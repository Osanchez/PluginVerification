import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Authentication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plugin_name = models.CharField(max_length=100)
    date_purchased = models.DateTimeField(default=timezone.now)
    authentic_key = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.user.__str__()


class Blacklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.__str__()
