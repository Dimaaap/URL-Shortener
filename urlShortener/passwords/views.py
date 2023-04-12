import logging

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from .forms import ResetPasswordForm, ChangePasswordForm
from .services import PasswordFormHandler

user_model = get_user_model()
logger = logging.getLogger(__name__)


def forgot_password_view(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            PasswordFormHandler.forgot_password_form_handle(form, request)
        else:
            logger.warning(form.errors)
    else:
        form = ResetPasswordForm()
    return render(request, 'passwords/forgot-password-reset.html', context={'form': form})


def reset_password_view(request, token: str):
    current_user = user_model.objects.get(email=request.session.get('email'))
    user = current_user.verify_reset_password_token(token)
    if not user:
        return redirect('index_page')
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            PasswordFormHandler.reset_password_form_handle(request, form, user)
        else:
            print(form.errors.as_data())
    else:
        form = ChangePasswordForm()
    return render(request, 'passwords/reset-password-page.html', {"form": form})

