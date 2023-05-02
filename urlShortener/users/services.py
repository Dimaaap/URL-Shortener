from django.contrib.auth import authenticate, login
from django.contrib import messages

from passwords.services import get_data_from_model
from account_settings.models import UserCodes


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
            return False
        elif user_active:
            return True
        else:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return False
    else:
        messages.error(request, "Invalid email or token")


class FormsHandler:

    @staticmethod
    def signup_form_handle(signup_form):
        user = signup_form.save(commit=False)
        user.set_password(signup_form.cleaned_data['password'])
        user.save()

    @staticmethod
    def signin_form_handle(request, signin_form):
        email = signin_form.cleaned_data['email']
        request.session['email'] = email
        password = signin_form.cleaned_data['password']
        request.session['password'] = password
        user = authenticate(email=email, password=password)
        tfa_state = user_handle(request, user)
        return tfa_state

    @staticmethod
    def account_form_handle(account_form, current_user):
        username = account_form.cleaned_data['username']
        email = account_form.cleaned_data['password']
        current_user.username = username
        current_user = email
        current_user.save()

    @staticmethod
    def upload_avatar_form_handler(request, current_user):
        user_avatar = request.FILES['avatar']
        current_user.avatar = user_avatar
        current_user.save()

    @staticmethod
    def input_tfa_token_form_handler(request, tfa_form, totp, user_codes):
        token = tfa_form.cleaned_data['token']
        user_email = request.session.get('email')
        user_password = request.session.get('password')
        user = authenticate(email=user_email, password=user_password)
        is_valid_token = totp.verify(token)
        if user:
            if is_valid_token:
                login(request, user)
                messages.success(request, "You have been successfully logged in")
            elif token in user_codes.codes:
                login(request, user)
                user_codes.inactive_code(token)
                messages.success(request, 'You have been successfully logged in')
            else:
                messages.error(request, 'Incorrect token')
        else:
            messages.error(request, "Don`t match credentials")
