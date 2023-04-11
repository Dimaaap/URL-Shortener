import pyotp

from .filters import EqualFilter
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect


def get_data_from_model(model: callable, field: str, value):
    eq_filter = EqualFilter()
    try:
        result = model.objects.get(**eq_filter(field, value))
    except ObjectDoesNotExist:
        return False
    return result


class TokenGenerator:
    __user_model = get_user_model()

    @staticmethod
    def generate_totp_secret():
        totp_secret = pyotp.random_base32()
        return totp_secret

    @staticmethod
    def generate_totp_uri(user, issuer_name="UrlShorten"):
        totp_secret = user.usercodes.secret_key
        totp = pyotp.TOTP(totp_secret)
        return totp.provisioning_uri(user.email, issuer_name=issuer_name)
