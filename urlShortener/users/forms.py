from django import forms
from django.contrib.auth import get_user_model

user_model = get_user_model()


class SignInForm(forms.ModelForm):

    class Meta:
        model = user_model
        fields = ('username', )
