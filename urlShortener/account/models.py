from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()


class UserCodes(models.Model):
    secret_key = models.CharField(max_length=255)
    user = models.OneToOneField(user_model, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

