from django.contrib.auth.models import AbstractUser
from django.db import models

from market.common import get_uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=get_uuid())
    mobile_number = models.CharField(max_length=12, unique=True)
    email = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
