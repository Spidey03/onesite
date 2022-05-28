from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True)
    mobile_number = models.CharField(max_length=12, unique=True)
    email = models.CharField(unique=True, max_length=30)

    REQUIRED_FIELDS = ['id', 'first_name', 'last_name', 'email', 'mobile_number']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
