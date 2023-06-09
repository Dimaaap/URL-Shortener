from django import forms
from django.contrib.auth import get_user_model

from passwords.services import get_data_from_model

user_model = get_user_model()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = user_model
        fields = ('username', 'email', 'password')

    username = forms.CharField(label="Your name:",
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Your Email: ",
                             required=True,
                             widget=forms.EmailInput(attrs={"class": 'form-control'}))
    password = forms.CharField(label="Your password: ",
                               required=True,
                               min_length=6,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_repeat = forms.CharField(label='Repeat the password: ',
                                      required=True,
                                      min_length=6,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password(self):
        password = self.cleaned_data['password']
        if all([i.isdigit() for i in password]) or all([i.isalpha() for i in password]):
            raise forms.ValidationError('The password must contain letters and numbers')
        return password

    def clean_password_repeat(self):
        try:
            password = self.cleaned_data['password']
        except KeyError:
            return
        password_repeat = self.cleaned_data['password_repeat']
        if password != password_repeat:
            raise forms.ValidationError("Passwords must be equal")
        return password_repeat


class LogInForm(forms.Form):
    email = forms.EmailField(label='Email:', required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password:', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    remember_me = forms.BooleanField(label='Remember me', required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            get_data_from_model(user_model, 'email', email)
        except Exception:
            raise forms.ValidationError("Неправильний email")
        return email


class TFATokenForm(forms.Form):
    token = forms.CharField(label="Authentication Token", min_length=6, max_length=8,
                            required=True,
                            widget=forms.TextInput(attrs={"class": "form-control"}))


class UploadAvatarForm(forms.Form):
    avatar = forms.ImageField(label='', widget=forms.FileInput(), required=False)


class UserInformationForm(forms.ModelForm):
    class Meta:
        model = user_model
        fields = ('username', 'email')

    username = forms.CharField(label='Name', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
