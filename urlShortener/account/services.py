from io import BytesIO
import base64

import qrcode

from .models import UserCodes
from passwords.services import get_data_from_model


def form_qrcode_service(current_user):
    img_qrcode, totp_secret = create_qr_code_service(current_user)
    buffer = BytesIO()
    img_qrcode.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return img_base64, totp_secret


def create_qr_code_service(current_user):
    user_code = get_data_from_model(UserCodes, 'user', current_user)
    totp_secret = user_code.secret_key
    totp_uri = user_code.get_totp_uri()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(totp_uri)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color="white")
    return img, totp_secret
