from django import forms

from .models import URLDomains


class URLShortenForm(forms.Form):
    long_url_field = forms.URLField(label="Input a long URL:",
                                    required=True,
                                    widget=forms.URLInput(attrs={"class": "url-input",
                                                                 "id": "long_url_field",
                                                                 "placeholder": "Enter a long link here"
                                                                 }))
    domain_name = forms.CharField(label="Customize your link:",
                                  widget=forms.TextInput(attrs={"class": "domain-input",
                                                                "id": "domain-input-field"}))
    alias = forms.CharField(label="",
                            required=False,
                            widget=forms.TextInput(attrs={"class": "alias-field",
                                                          "placeholder": "Enter alias",
                                                          "id": "alias-input-field"
                                                          }))

    def clean_domain_name(self):
        domain_name = self.cleaned_data['domain_name']
        if domain_name.strip() != "shortenurl.com":
            raise forms.ValidationError("Incorrect domain name")
        return domain_name

    def clean_alias(self):
        alias = self.cleaned_data['alias']
        if not alias:
            return alias
        forbid_chars = '-.,!@#%$^&*();"\\/'
        filter_list = filter(lambda char: char in forbid_chars, list(alias))
        if filter_list:
            raise forms.ValidationError("Incorrect alias name")
        return alias
