import logging

import pyotp
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


from .forms import *
from .decorators import redirect_login_users
from .models import User
from account_settings.models import UserCodes, UsersBackupCodes
from .services import FormsHandler
from account_settings.services import try_get_current_user, get_data_from_model

logger = logging.getLogger(__name__)
user_model = get_user_model()


@redirect_login_users
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            FormsHandler.signup_form_handle(form)
            return redirect('signin')
        else:
            logger.error(f"Sing Up Form is invalid - {form.errors}")
    else:
        form = SignUpForm()
    return render(request, template_name='users/signup.html', context={'form': form})


@redirect_login_users
def signin_view(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            tfa_state = FormsHandler.signin_form_handle(request, form)
            if tfa_state:
                return redirect('tfa-input')
        else:
            logger.error(f"Login form`s error - {form.errors}")
    else:
        form = LogInForm()
    return render(request, template_name='users/signin.html', context={'form': form})


@redirect_login_users
def tfa_input_view(request):
    current_user = get_data_from_model(user_model, 'email', request.session.get('email'))
    user_secret_key = get_data_from_model(UserCodes, 'user', current_user)
    user_backup_codes = get_data_from_model(UsersBackupCodes, 'user', current_user)
    totp = pyotp.TOTP(user_secret_key.secret_key, issuer=current_user.email)
    if request.method == 'POST':
        form = TFATokenForm(request.POST)
        if form.is_valid():
            FormsHandler.input_tfa_token_form_handler(request, form, totp, user_backup_codes)
        else:
            logger.error(f'Form {form} error')
    else:
        form = TFATokenForm()
    return render(request, template_name='users/tfa-input.html', context={'form': form})


@login_required(login_url='signin')
def account_view(request, url_username):
    current_user = get_object_or_404(User, url_username=url_username)
    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        if form.is_valid():
            FormsHandler.account_form_handle(form, current_user)
            logger.info("Users`s information has been saved successful")
        else:
            logger.error("User information form error")
    else:
        form = UserInformationForm(initial={'username': current_user.username,
                                            'email': current_user.email})
    context = {'form': form, 'second_form': UploadAvatarForm(request.POST or None),
               'user_avatar': current_user.avatar}
    return render(request, template_name='users/account.html', context=context)


@login_required(login_url='signin')
def upload_avatar_form(request, url_username):
    try:
        current_user = User.objects.get(url_username=url_username)
    except ObjectDoesNotExist:
        logger.warning("The user doesn`t find")
        return redirect('account_settings', url_username)
    if request.method == 'POST':
        form = UploadAvatarForm(request.POST)
        if form.is_valid():
            FormsHandler.upload_avatar_form_handler(request, current_user)
        else:
            logger.warning(form.errors)
    return redirect('account_settings', url_username)


def facebook_login_view(request):
    pass


@login_required
def logout_users(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='signin')
# TODO:ЗРОБИТИ МОЖЛИВІСТЬ КОРИСТУВАЧАМ ВИДАЛЯТИ СВОЇ ОБЛІКОВІ ЗАПИСИ
def delete_account(request, url_username):
    pass
