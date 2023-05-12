from django import forms

from passwords.forms import ChangePasswordForm


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
    OPPORTUNITIES = (('Create ShortenURL', '1 '),
                     ('Update ShortenURL', '2'),
                     ('Archive ShortenURL', '3'))

    token_name = forms.CharField(max_length=40, min_length=2, required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    token_opportunity = forms.CharField(widget=forms.Select(choices=OPPORTUNITIES))

