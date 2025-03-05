import logging

from .models import OpenAIRequestLog


logger = logging.getLogger(__name__)


def log_openai_request(endpoint, request_data, response_data=None, status_code=None):
    """Log an OpenAI API request to the database."""
    try:
        log_entry = OpenAIRequestLog.objects.create(
            endpoint=endpoint,
            request_data=request_data,
            response_data=response_data,
            status_code=status_code or 500
        )
        return log_entry
    except Exception as e:
        logger.error(f"Error logging OpenAI request: {str(e)}")
        return None


def extract_response_data(response):
    try:
        return response.json()
    except Exception:
        return None
