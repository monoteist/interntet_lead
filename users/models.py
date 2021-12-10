from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.TextChoices):
    MANAGER = 'MANAGER'
    EMPLOYEE = 'EMPLOYEE'

class CustomUser(AbstractUser):
    role = models.CharField(max_length=8, choices=Role.choices)