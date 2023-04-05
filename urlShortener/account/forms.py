from django import forms

from passwords.forms import ChangePasswordForm


class UpdatePasswordForm(ChangePasswordForm):
    pass


class InputTokenForm(forms.Form):
    code = forms.CharField(max_length=6, required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
