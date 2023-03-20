from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from .forms import *


def signup_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            #form.save(commit=False)
            form.cleaned_data['user_password'] = make_password(form.cleaned_data['password'])
            form.save()
            return redirect('index_page')
    else:
        form = SignInForm()
    return render(request, template_name='users/signup.html', context={'form': form})
