import pyotp
from django.db import models
from django.contrib.auth import get_user_model

from users.models import User
from .generate_backup_codes import generate_user_backup_codes

user_model = get_user_model()


class UserCodes(models.Model):
    secret_key = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    totp_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.secret_key} - {self.totp_active}"

    def active_totp(self):
        self.totp_active = True
        self.save()

    def enable_totp(self):
        if not self.secret_key:
            self.secret_key = pyotp.random_base32()

    def disable_totp(self):
        self.totp_active = False
        self.save()

    def get_totp_uri(self):
        if not self.secret_key:
            self.enable_totp()
        totp = pyotp.TOTP(self.secret_key)
        return totp.provisioning_uri(name=self.user.username, issuer_name="URLShort")


class UsersBackupCodes(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    codes = models.JSONField(default=list, blank=True, null=True)
    codes_activate = models.BooleanField(default=False)

    def __str__(self):
        return self.codes_activate

    def generate_codes(self):
        if self.codes_activate:
            generated_codes = generate_user_backup_codes()
            self.codes = generated_codes
            self.save()


