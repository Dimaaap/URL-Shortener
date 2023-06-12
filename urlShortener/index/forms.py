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
                            widget=forms.TextInput(attrs={"class": "alias-field",
                                                          "placeholder": "Enter alias",
                                                          "id": "alias-input-field"
                                                          }))
