from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=False
    )
    email = models.EmailField(unique=True, max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

