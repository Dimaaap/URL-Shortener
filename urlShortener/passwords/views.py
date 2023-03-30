from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string

from .forms import ResetPasswordForm, ChangePasswordForm
from .services import get_data_from_model

user_model = get_user_model()


def forgot_password_view(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            try:
                current_user = get_data_from_model(user_model, 'email', user_email)
            except ObjectDoesNotExist:
                print("User input incorrect email")
                return redirect("signin")
            token = current_user.get_reset_password_token()
            request.session['token'] = token
            request.session['email'] = user_email
            html_message = render_to_string("passwords/email/reset-password.html",
                                            {"user": current_user, "token": token})
            send_mail(subject="Password Reset",
                      message="",
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[user_email],
                      html_message=html_message
                      )
            messages.success(request, "Password reset link has been sent to your email")
        else:
            print(form.errors)
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
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Your password has been changed successfully")
        else:
            print(form.errors.as_data())
    else:
        form = ChangePasswordForm()
    return render(request, 'passwords/reset-password-page.html', {"form": form})
