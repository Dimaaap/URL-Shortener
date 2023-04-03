from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UpdatePasswordForm

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
    return render(request, 'account/update-password.html', {'form': form})


@login_required(login_url='signin')
def tfa_enable_view(request, url_username):
    return render(request, "account/tfa-enable.html")