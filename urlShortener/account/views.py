import logging

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from pyotp import TOTP

from .forms import UpdatePasswordForm, InputTokenForm
from .services import *
from passwords.services import get_data_from_model

user_model = get_user_model()
logger = logging.getLogger(__name__)


@login_required(login_url='signin')
def update_password_view(request, url_username):
    try:
        current_user = user_model.objects.get(url_username=url_username)
    except ObjectDoesNotExist:
        logger.warning("Incorrect user data")
        return redirect('index_page')
    if request.method == 'POST' and "first-form" in request.POST:
        form = UpdatePasswordForm(request.POST)
        if form.is_valid():
            AccountFormsHandler.update_password_form_handle(request, form, current_user)
        else:
            logger.warning(form.errors)
    if request.method == 'POST':
        handle_tfw_form_service(request, url_username)
    form = UpdatePasswordForm()
    second_form = InputTokenForm()
    user_totp_enabled = get_data_from_model(UserCodes, 'user', current_user)
    img_base64, totp_secret = form_qrcode_service(current_user)
    return render(request, 'account/update-password.html',
                  {'form': form,
                   'second_form': second_form,
                   'qr_code': img_base64,
                   'totp_secret': totp_secret,
                   'tfa_enabled': user_totp_enabled.totp_active})


def handle_tfw_form_service(request, url_username):
    try:
        current_user = user_model.objects.get(url_username=url_username)
    except ObjectDoesNotExist:
        logger.warning("Incorrect user data")
        return redirect('index_page')
    user_secret_key = get_data_from_model(UserCodes, "user", current_user)
    if not user_secret_key.secret_key:
        user_secret_key.secret_key = user_secret_key.enable_totp()
        user_secret_key.save()
    totp = TOTP(user_secret_key.secret_key)
    second_form = InputTokenForm(request.POST)
    if second_form.is_valid():
        code = second_form.cleaned_data['code']
        is_valid = totp.verify(code)
        if is_valid:
            user_secret_key.active_totp()
        else:
            messages.error(request, "Invalid token")
    else:
        logger.warning(second_form.errors)
