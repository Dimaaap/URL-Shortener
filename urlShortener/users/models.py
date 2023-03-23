from random import randint

from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=False
    )
    url_username = models.CharField(max_length=150, null=True, default=None)
    email = models.EmailField(unique=True, max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        split_email = str(self.email).split("@")[0]
        self.url_username = split_email + str(randint(1, 100))
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email


class UserPersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', max_length=250, null=True, default=None)

    def __str__(self):
        return self.user


