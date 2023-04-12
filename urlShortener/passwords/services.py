import pyotp

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .filters import EqualFilter


def get_data_from_model(model: callable, field: str, value):
    eq_filter = EqualFilter()
    try:
        result = model.objects.get(**eq_filter(field, value))
    except ObjectDoesNotExist:
        return False
    return result


def get_current_user(user_email):
    try:
        current_user = get_data_from_model(get_user_model(), 'email', user_email)
        return current_user
    except ObjectDoesNotExist:
        return redirect('signin')


def set_data_in_session(request, **kwargs):
    for key, value in kwargs.items():
        request.session[key] = value


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


class PasswordFormHandler:

    @staticmethod
    def forgot_password_form_handle(forgot_password_form, request):
        user_email = forgot_password_form.cleaned_data['email']
        current_user = get_current_user(user_email) or None
        token = current_user.get_reset_password_token()
        set_data_in_session(request, token=token, email=user_email)
        html_message = render_to_string('passwords/email/reset-password.html',
                                        {"user": current_user, "token": token})
        send_mail(subject="Password Reset",
                  message="",
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[user_email],
                  html_message=html_message)
        messages.success(request, "Password reset link has been sent to your email")

    @staticmethod
    def reset_password_form_handle(request, reset_password_form, user):
        user.set_password(reset_password_form.cleaned_data['password'])
        user.save()
        messages.success(request, "Your password has been changed successfully")
