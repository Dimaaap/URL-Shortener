from pathlib import Path
import string
import secrets
import uuid

import pyotp
from django.db import models
from django.core.files import File
from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone

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
    codes_file = models.FileField(upload_to='codes/%Y-%m-%d/', null=True, default=None)

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

    def create_file(self):
        content = 'Hello World'.encode('utf-8')
        file = ContentFile(content)
        self.codes_file.save(f'{self.user.url_username}_codes.txt', file)

    def write_codes_into_file(self):
        if not self.codes_file:
            self.create_file()
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


class UserAPITokens(models.Model):
    SECRET_KEY_LEN = 60

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    token_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now=True)
    can_create = models.BooleanField(default=True)
    can_update = models.BooleanField(default=False)
    can_archive = models.BooleanField(default=False)
    generated_key = models.CharField(max_length=61, null=True)

    def __str__(self):
        return self.token_name

    def compare_created_and_used_time(self):
        localize_created = timezone.localtime(self.created_at)
        localize_used = timezone.localtime(self.last_used)
        formatted_created = localize_created.strftime("%Y-%m-%d %H:%M:%S")
        formatted_used = localize_used.strftime("%Y-%m-%d %H:%M:%S")
        if formatted_used == formatted_created:
            return True
        return False

    def generate_secret_key(self):
        characters = string.ascii_letters
        random_string = ''.join(secrets.choice(characters) for _ in range(self.SECRET_KEY_LEN))
        self.generated_key = random_string
        self.save()


