import json
import os
import requests

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .utils import log_openai_request, extract_response_data

@csrf_exempt
@require_http_methods(["POST"])
def openai_proxy(request, path=''):
    """
    A 1:1 API proxy endpoint for OpenAI API calls. Forwards the request exactly as received to OpenAI API.
    
    Logs all requests to the database for monitoring and analytics.
    
    TODO: allow GET requests
    TODO: make OpenAI api key optional, set as env variable, if debug=True and openai key optional then use debug key, else error
    """
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return JsonResponse({"error": "OpenAI API key not found in environment variables"}, status=500)
        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            error_message = "Invalid JSON in request body"
            log_openai_request(
                endpoint=path if path else "chat/completions",
                request_data={"raw_body": request.body.decode('utf-8', errors='ignore')},
                response_data={"error": error_message},
                status_code=400
            )
            return JsonResponse({"error": error_message}, status=400)
        
        # set default model
        if "model" not in body:
            body["model"] = "gpt-4o"
        
        headers = {}
        for key, value in request.headers.items():
            if key.lower() not in ['host', 'content-length', 'authorization']:
                headers[key] = value
        
        headers["Authorization"] = f"Bearer {api_key}"
        headers["Content-Type"] = "application/json"
        
        if path:
            openai_url = f"https://api.openai.com/v1/{path}"
        else:
            openai_url = "https://api.openai.com/v1/chat/completions"
        
        # make end request
        response = requests.post(
            openai_url,
            headers=headers,
            json=body
        )

        response_data = extract_response_data(response)
            
        django_response = HttpResponse(
            content=response.content,
            status=response.status_code,
            content_type=response.headers.get('Content-Type', 'application/json')
        )
        
        for key, value in response.headers.items():
            if key.lower() not in ['content-length', 'connection', 'transfer-encoding']:
                django_response[key] = value
        
        log_openai_request(
            endpoint=path if path else "chat/completions",
            request_data=body,
            response_data=response_data,
            status_code=response.status_code
        )
        
        return django_response
    
    except Exception as e:
        error_message = str(e)
        log_openai_request(
            endpoint=path if path else "chat/completions",
            request_data=body if 'body' in locals() else {},
            response_data={"error": error_message},
            status_code=500
        )
            
        return JsonResponse({"error": error_message}, status=500)
