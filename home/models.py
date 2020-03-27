from django.conf import settings
from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField()
    message = models.TextField()
