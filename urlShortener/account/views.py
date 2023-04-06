from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UpdatePasswordForm, InputTokenForm
from .services import *

user_model = get_user_model()


@login_required(login_url='signin')
def update_password_view(request, url_username):
    try:
        current_user = user_model.objects.get(url_username=url_username)
    except ObjectDoesNotExist:
        print("Incorrect user data")
        return redirect('index_page')

    if request.method == 'POST':
        form = UpdatePasswordForm(request.POST)
        if form.is_valid():
            user_password = form.cleaned_data['password']
            current_user.set_password(user_password)
            current_user.save()
            messages.success(request, "Your password has been updated successfully")
        else:
            print(form.errors)
    else:
        form = UpdatePasswordForm()

    img_base64, totp_secret = form_qrcode_service(current_user)
    return render(request, 'account/update-password.html',
                  {'form': form,
                   'second_form': InputTokenForm(request.POST or None),
                   'qr_code': img_base64,
                   'totp_secret': totp_secret})


def input_code_form_view(request, url_username):
    try:
        current_user = user_model.objects.get(url_username=url_username)
    except ObjectDoesNotExist:
        print("Incorrect user data")
        return redirect('index_page')
    print("dsadsa")
    if request.method == 'POST':
        form = InputTokenForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['code'])
        else:
            print(form.errors)
    return redirect('update-password', url_username=url_username)
