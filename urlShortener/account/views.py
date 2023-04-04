from io import BytesIO

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pyqrcode

from .forms import UpdatePasswordForm, InputTokenForm
from .models import UserCodes

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
    buffer = BytesIO()
    qr_code, totp_secret = create_qr_code_service(current_user)
    qr_code_svg = qr_code.svg(buffer, scale=5)
    buffer_value = buffer.getvalue()
    print(buffer_value)
    return render(request, 'account/update-password.html', {'form': form,
                                                            'qr_code': buffer_value,
                                                            'totp_secret': totp_secret})


# @login_required(login_url='signin')
# def tfa_enable_view(request, url_username):
#     current_user = user_model.objects.get(url_username=url_username)
#     user_code = UserCodes.objects.get(user=current_user)
#     totp_secret = user_code.secret_key
#     totp_uri = user_code.get_totp_uri()
#     qr_code = pyqrcode.create(totp_uri)
#     context = {'qr_code': qr_code.svg(), 'totp_secret': totp_secret}
#     return render(request, "account/tfa-enable.html", context)

def create_qr_code_service(current_user):
    user_code = UserCodes.objects.get(user=current_user)
    totp_secret = user_code.secret_key
    totp_uri = user_code.get_totp_uri()
    qr_code = pyqrcode.create(totp_uri)
    return qr_code, totp_secret

