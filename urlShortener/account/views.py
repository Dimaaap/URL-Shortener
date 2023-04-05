from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
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
        form = UpdatePasswordForm(request.POST, prefix='first')
        if form.is_valid():
            user_password = form.cleaned_data['password']
            current_user.set_password(user_password)
            current_user.save()
            messages.success(request, "Your password has been updated successfully")
        else:
            print(form.errors)
    else:
        form = UpdatePasswordForm(prefix='first')

    if request.method == 'POST' and not form.is_valid():
        second_form = InputTokenForm(request.POST, prefix='second')
        if second_form.is_valid():
            pass
        else:
            print(second_form.errors)
    else:
        second_form = InputTokenForm(prefix='second')

    img_base64, totp_secret = form_qrcode_service(current_user)
    return render(request, 'account/update-password.html', {'form': form,
                                                            'second_form': second_form,
                                                            'qr_code': img_base64,
                                                            'totp_secret': totp_secret})




