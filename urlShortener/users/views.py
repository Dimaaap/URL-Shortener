from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import *
from .decorators import redirect_login_users
from .models import User


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
                login(request, user)
                messages.success(request, "Авторизація пройшла успішно")
            else:
                print('12321321321312')
    else:
        form = LogInForm()
    return render(request, template_name='users/signin.html', context={'form': form})


def account_view(request, url_username):
    current_user = get_object_or_404(User, url_username=url_username)
    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = UserInformationForm()
    context = {'form': form, 'second_form': UploadAvatarForm(request.POST or None),
               'user_avatar': current_user.avatar}
    return render(request, template_name='users/account.html', context=context)


def upload_avatar_form(request, url_username):
    if request.method == 'POST':
        form = UploadAvatarForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = UploadAvatarForm()
    return redirect('account')