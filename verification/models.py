import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Authentic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    plugin_name = models.CharField(max_length=100)
    date_purchased = models.DateField(auto_now_add=True)
    authentic_key = models.UUIDField(default=uuid.uuid4, editable=False)
