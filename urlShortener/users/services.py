from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from passwords.services import get_data_from_model
from account.models import UserCodes


def is_user_tfa_active(user):
    user_code = get_data_from_model(UserCodes, 'user', user)
    if not user_code:
        return None
    return True if user_code.totp_active else False


def user_handle(request, user):
    if user:
        user_active = is_user_tfa_active(user)
        if user_active is None:
            messages.error(request, "Invalid credentials")
        elif user_active:
            return redirect("tfa-input")
        else:
            login(request, user)
            messages.success(request, "You have successfully logged in")
    else:
        messages.error(request, "Invalid email or token")


class FormsHandler:

    @staticmethod
    def signup_form_handle(signup_form):
        user = signup_form.save(commit=False)
        user.set_password(signup_form.cleaned_data['password'])
        user.save()
        new_user_code = UserCodes(user=user)
        new_user_code.enable_totp()
        new_user_code.save()

    @staticmethod
    def signin_form_handle(request, signin_form):
        email = signin_form.cleaned_data['email']
        password = signin_form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        user_handle(request, user)

    @staticmethod
    def account_form_handle(account_form, current_user):
        username = account_form.cleaned_data['username']
        email = account_form.cleaned_data['password']
        current_user.username = username
        current_user = email
        current_user.save()