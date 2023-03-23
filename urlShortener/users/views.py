from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import *
from .decorators import redirect_login_users


@redirect_login_users
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('index_page')
    else:
        form = SignUpForm()
    return render(request, template_name='users/signup.html', context={'form': form})


@redirect_login_users
def signin_view(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                print('dsadsadas')
                login(request, user)
                messages.success(request, "Авторизація пройшла успішно")
            else:
                print('12321321321312')
    else:
        form = LogInForm()
    return render(request, template_name='users/signin.html', context={'form': form})


def account_view(request):
    if request.method == 'POST':
        form = UploadAvatarForm(request.POST)
    else:
        form = UploadAvatarForm()
    return render(request, template_name='users/account.html', context={'form': form})
