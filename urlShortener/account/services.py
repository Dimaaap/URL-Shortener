from io import BytesIO
import base64

import qrcode
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .models import UserCodes
from passwords.services import get_data_from_model


def form_qrcode_service(current_user):
    img_qrcode, totp_secret = create_qr_code_service(current_user)
    buffer = BytesIO()
    img_qrcode.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return img_base64, totp_secret


def create_user_code(current_user):
    try:
        user_code = get_data_from_model(UserCodes, 'user', current_user)
        return user_code
    except ObjectDoesNotExist:
        new_user_code = UserCodes(user=current_user)
        new_user_code.enable_totp()
        new_user_code.save()
        return new_user_code


def create_qr_code_service(current_user):
    user_code = create_user_code(current_user)
    totp_secret = user_code.secret_key
    totp_uri = user_code.get_totp_uri()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(totp_uri)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color="white")
    return img, totp_secret


class AccountFormsHandler:

    @staticmethod
    def update_password_form_handle(request, update_password_form, current_user):
        user_password = update_password_form.cleaned_data['password']
        current_user.set_password(user_password)
        current_user.save()
        messages.success(request, "Your password has been changed successfully")
