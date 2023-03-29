from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import ResetPasswordForm



def forgot_password_view(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            send_mail(subject="Password Reset",
                      message="dasdsadasds",
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[user_email]
                      )
        else:
            print(form.errors)
    else:
        form = ResetPasswordForm()
    return render(request, 'passwords/forgot-password-reset.html', context={'form': form})


def reset_password_view(request, token: str):
    user = request.user
    return render(request, 'passwords/reset-password-page.html')
