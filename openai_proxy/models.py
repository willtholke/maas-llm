import uuid

from django.db import models
from django.utils import timezone


class OpenAIRequestLog(models.Model):
    """Rudimentary model for logging OpenAI API requests"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(default=timezone.now)
    endpoint = models.CharField(max_length=255, help_text="OpenAI API endpoint that was called")
    request_data = models.JSONField(help_text="Full request data sent to OpenAI")
    response_data = models.JSONField(help_text="Full response data received from OpenAI", null=True, blank=True)
    status_code = models.IntegerField(help_text="HTTP status code of the response")
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.endpoint} - {self.timestamp}"
