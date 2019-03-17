import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Authentication(models.Model):
    authentic_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.CharField(max_length=100, default='')
    plugin_name = models.CharField(max_length=100)
    date_purchased = models.DateTimeField(default=timezone.now)
    black_listed = models.BooleanField(default=False)

    def __str__(self):
        return self.authentic_key.__str__()

