import jwt
from random import randint
from time import time

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from .managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=False
    )
    url_username = models.CharField(max_length=150, null=True, default=None)
    email = models.EmailField(unique=True, max_length=255)
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d', max_length=250, null=True, default=None)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        split_email = str(self.email).split("@")[0]
        if not self.url_username:
            self.url_username = split_email + str(randint(1, 100))
        super(User, self).save(*args, **kwargs)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode({
            "reset_password": self.pk, "exp": time() + expires_in
        }, settings.SECRET_KEY, algorithm="HS256"
        )

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])['reset_password']
        except Exception as e:
            print(e)
            return
        return User.objects.get(pk=id)
