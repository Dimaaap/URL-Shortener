from pathlib import Path

import pyotp
from django.db import models
from django.core.files import File
from django.contrib.auth import get_user_model
from django.conf import settings

from .generate_backup_codes import generate_user_backup_codes

user_model = get_user_model()


class UserCodes(models.Model):
    secret_key = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(user_model, on_delete=models.CASCADE)
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
        totp = pyotp.TOTP(self.secret_key, issuer=self.user.email)
        return totp.provisioning_uri(name=self.user.email, issuer_name="URLShort")


class UsersBackupCodes(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    codes = models.JSONField(default=list, blank=True, null=True)
    codes_active = models.BooleanField(default=False)
    generate_date = models.DateTimeField(auto_now=True)
    codes_file = models.FileField(upload_to='codes/%Y-%m-d/', null=True, default=None)

    def __str__(self):
        return f'{self.user} - {self.codes_active}'

    def generate_codes(self):
        if self.codes_active and not self.codes:
            generated_codes = generate_user_backup_codes()
            self.codes = generated_codes
            self.save()

    def delete_codes(self):
        if self.codes:
            self.codes = None
            self.codes_active = False
            self.save()

    def write_codes_into_file(self):
        path = Path(self.codes_file.path)
        with path.open(mode='a+') as file:
            codes_file = File(file)
            codes_file.truncate(0)
            codes_file.write(settings.PRE_TEXT)
            for code in self.codes:
                codes_file.write(code + "\n")
            codes_file.write(settings.POST_TEXT + ' ' + str(self.generate_date)[:19])

    def inactive_code(self, code: str):
        if code in self.codes:
            self.codes.remove(code)
            self.save()
