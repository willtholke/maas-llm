import os
import json
import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["POST"])
def openai_proxy(request, path=''):
    """
    A 1:1 API proxy endpoint for OpenAI API calls. Forwards the request exactly as received to OpenAI API, only adding the API key.

    TODO: log requests to supabase
    TODO: allow GET requests
    """
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return JsonResponse({"error": "OpenAI API key not found in environment variables"}, status=500)
        
        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON in request body"}, status=400)
        
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
            
        response = requests.post(
            openai_url,
            headers=headers,
            json=body
        )
        
        django_response = HttpResponse(
            content=response.content,
            status=response.status_code,
            content_type=response.headers.get('Content-Type', 'application/json')
        )
        
        for key, value in response.headers.items():
            if key.lower() not in ['content-length', 'connection', 'transfer-encoding']:
                django_response[key] = value
        
        return django_response
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
