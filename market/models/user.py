from datetime import datetime

from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    joined_at = models.DateTimeField(blank=True, null=True)
    mobile_number = models.CharField(max_length=12, unique=True)
    email = models.CharField(unique=True, max_length=30)