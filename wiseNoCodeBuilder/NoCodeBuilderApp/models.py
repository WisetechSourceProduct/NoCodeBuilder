import uuid
from django.db import models
import datetime as dt

# Create your models here.

class Pages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    html = models.TextField()
    css = models.TextField()
    created_at = models.DateTimeField(default=dt.datetime.now())
    updated_at = models.DateTimeField(default=dt.datetime.now())

    def __str__(self):
        return self.name
    

class FormSubmission(models.Model):
    form_data = models.JSONField()  # Storing form data as JSON

    def __str__(self):
        return str(self.form_data)