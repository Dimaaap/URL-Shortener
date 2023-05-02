from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import UsersBackupCodes

user_model = get_user_model()


@receiver(post_save, sender=user_model)
def post_save_create_user_backup_codes(sender, instance, created, **kwargs):
    if created:
        new_user_backup_codes = UsersBackupCodes(user=instance)
        new_user_backup_codes.save()
