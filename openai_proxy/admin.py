from django.contrib import admin
from .models import OpenAIRequestLog

@admin.register(OpenAIRequestLog)
class OpenAIRequestLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'endpoint', 'status_code')
    list_filter = ('endpoint', 'status_code')
    search_fields = ('endpoint',)
    readonly_fields = ('id', 'timestamp', 'endpoint', 'request_data', 'response_data', 'status_code')
    ordering = ('-timestamp',)
