import pyperclip

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import FileResponse

from .forms import UpdatePasswordForm
from .services import *
from passwords.services import get_data_from_model

logger = logging.getLogger(__name__)


@login_required(login_url='signin')
def update_password_view(request, url_username):
    current_user = try_get_current_user(url_username)
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
    # user_totp_enabled = get_data_from_model(UserCodes, 'user', current_user)
    user_totp_enabled = UserCodes.objects.select_related('user').get(user=current_user)
    img_base64, totp_secret = form_qrcode_service(current_user)
    # backup_user_codes = get_data_from_model(UsersBackupCodes, "user", current_user)
    backup_user_codes = UsersBackupCodes.objects.select_related('user').get(user=current_user)
    if not backup_user_codes.codes:
        codes_active = False
        generated_codes = None
    else:
        codes_active = True
        generated_codes = backup_user_codes.codes
    return render(request, 'account/update-password.html',
                  {'form': form,
                   'second_form': second_form,
                   'qr_code': img_base64,
                   'totp_secret': totp_secret,
                   'tfa_enabled': user_totp_enabled.totp_active,
                   'generate_codes_service': generated_codes,
                   'generate_date': backup_user_codes.generate_date or None,
                   'codes_active': codes_active})


def disable_tfa_view(request, url_username):
    current_user = try_get_current_user(url_username)
    user_code = get_data_from_model(UserCodes, 'user', current_user)
    user_code.disable_totp()
    return redirect('update-password', url_username)


def save_code_view(request, url_username):
    current_user = try_get_current_user(url_username)
    user_codes = get_data_from_model(UsersBackupCodes, 'user', current_user)
    user_codes.write_codes_into_file()
    codes_file = user_codes.codes_file
    return FileResponse(codes_file, as_attachment=True)


def copy_codes_to_clipboard_view(request, url_username):
    current_user = try_get_current_user(url_username)
    backup_user_codes = get_data_from_model(UsersBackupCodes, 'user', current_user)
    user_codes = backup_user_codes.codes
    codes_string = form_code_string_service(user_codes)
    pyperclip.copy(codes_string)
    messages.success(request, "Your codes have been successfully copied to clipboard")
    return redirect('update-password', url_username)


def generate_backup_codes_view(request, url_username):
    current_user = try_get_current_user(url_username)
    backup_user_codes = get_data_from_model(UsersBackupCodes, "user", current_user)
    backup_user_codes.codes_active = True
    backup_user_codes.generate_codes()
    return redirect(update_password_view, url_username)


def generate_new_codes_view(request, url_username):
    current_user = try_get_current_user(url_username)
    backup_user_codes = get_data_from_model(UsersBackupCodes, 'user', current_user)
    backup_user_codes.codes = []
    backup_user_codes.generate_codes()
    return redirect(update_password_view, url_username)


def delete_codes_view(request, url_username):
    current_user = try_get_current_user(url_username)
    user_backup_codes = get_data_from_model(UsersBackupCodes, 'user', current_user)
    user_backup_codes.delete_codes()
    request.session['gen_codes'] = False
    return redirect(update_password_view, url_username)
