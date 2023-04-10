from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pyotp import TOTP

from .forms import UpdatePasswordForm, InputTokenForm
from .services import *
from passwords.services import get_data_from_model

user_model = get_user_model()


@login_required(login_url='signin')
def update_password_view(request, url_username):
    try:
        current_user = user_model.objects.get(url_username=url_username)
    except ObjectDoesNotExist:
        print("Incorrect user data")
        return redirect('index_page')

    if request.method == 'POST' and "first-form" in request.POST:
        form = UpdatePasswordForm(request.POST)
        if form.is_valid():
            user_password = form.cleaned_data['password']
            current_user.set_password(user_password)
            current_user.save()
            messages.success(request, "Your password has been updated successfully")
        else:
            print(form.errors)
    if request.method == 'POST':
        handle_tfw_form_service(request, url_username)
    form = UpdatePasswordForm()
    second_form = InputTokenForm()
    user_totp_enabled = get_data_from_model(UserCodes, 'user', current_user)
    print(user_totp_enabled.totp_active)
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
        print("Incorrect user data")
        return redirect('index_page')
    user_secret_key = UserCodes.objects.get(user=current_user)
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
        print(second_form.errors)
