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


class CustomAbstractBooleanField(forms.BooleanField):

    def __init__(self, label, initial=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = label
        self.initial = initial
        self.required = False
        self.widget = forms.CheckboxInput(attrs={'class': 'field-checknox'})


class AbstractTokenForm(forms.Form):
    token_name = forms.CharField(max_length=40, min_length=2, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    can_create = CustomAbstractBooleanField(label="Create ShortURL", initial=True)
    can_update = CustomAbstractBooleanField(label="Update ShortURL")
    can_archive = CustomAbstractBooleanField(label="Archive ShortURL")


class CreateTokenForm(AbstractTokenForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_token_name(self):
        token_name = self.cleaned_data['token_name']
        try:
            UserAPITokens.objects.get(user=self.user, token_name=token_name)
        except ObjectDoesNotExist:
            return token_name
        raise forms.ValidationError(f"The token with name {token_name} already exist")


class EditTokenForm(AbstractTokenForm):
    pass
