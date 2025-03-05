# Generated by Django 5.1.6 on 2025-03-05 05:26

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OpenAIRequestLog",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "endpoint",
                    models.CharField(
                        help_text="OpenAI API endpoint that was called", max_length=255
                    ),
                ),
                (
                    "request_data",
                    models.JSONField(help_text="Full request data sent to OpenAI"),
                ),
                (
                    "response_data",
                    models.JSONField(
                        blank=True,
                        help_text="Full response data received from OpenAI",
                        null=True,
                    ),
                ),
                (
                    "status_code",
                    models.IntegerField(help_text="HTTP status code of the response"),
                ),
            ],
            options={
                "ordering": ["-timestamp"],
            },
        ),
    ]
