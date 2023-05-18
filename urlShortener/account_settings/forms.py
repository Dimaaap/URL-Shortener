from django import forms
from django.core.exceptions import ObjectDoesNotExist

from passwords.forms import ChangePasswordForm
from .models import UserAPITokens


class UpdatePasswordForm(ChangePasswordForm):
    pass


class InputTokenForm(forms.Form):
    code = forms.CharField(min_length=6, max_length=6, required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_code(self):
        code = self.cleaned_data['code']
        if len(code) < 6:
            raise forms.ValidationError("The code must contain exactly 6 symbols")
        return code


class CreateTokenForm(forms.Form):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    token_name = forms.CharField(max_length=40, min_length=2, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    can_create = forms.BooleanField(label="Create ShortURL", initial=True, required=False,
                                    widget=forms.CheckboxInput(attrs={'class': 'field-checkbox'}))
    can_update = forms.BooleanField(label="Update ShortURL", required=False,
                                    widget=forms.CheckboxInput(attrs={'class': 'field-checkbox'}))
    can_archive = forms.BooleanField(label="Archive ShortURL", required=False,
                                     widget=forms.CheckboxInput(attrs={'class': 'field-checkbox'}))

    def clean_token_name(self):
        token_name = self.cleaned_data['token_name']
        try:
            UserAPITokens.objects.get(user=self.user, token_name=token_name)
        except ObjectDoesNotExist:
            return token_name
        raise forms.ValidationError(f"The token with name {token_name} already exist")




