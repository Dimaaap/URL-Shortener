from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

user_model = get_user_model()


class ResetPasswordForm(forms.Form):
    email = forms.EmailField(label="E-Mail Address",
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user_model.objects.get(email=email)
        except ObjectDoesNotExist:
            raise forms.ValidationError("Incorrect email")
        return email


class ChangePasswordForm(forms.Form):
    password = forms.CharField(required=True, label="Your Password",
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password_repeat = forms.CharField(required=True, label="Repeat Your Password",
                                      widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean_password(self):
        password = self.cleaned_data['password']
        if all([i.isdigit() for i in password]) or all([i.isalpha() for i in password]):
            raise forms.ValidationError('The password must contain letters and numbers')
        return password
