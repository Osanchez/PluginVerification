import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Plugin(models.Model):
    plugin_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default='')
    author = models.CharField(max_length=100, default='')
    description = models.TextField()
    download_link = models.CharField(max_length=255, default='')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title.__str__()

