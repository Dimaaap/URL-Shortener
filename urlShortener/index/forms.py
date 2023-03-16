from django import forms

from .models import URLDomains


class URLShortenForm(forms.Form):
    user_email = forms.URLField(label="Your long URL",
                                widget=forms.URLInput(attrs={"class": "form-control"}))
    shorten_email = forms.URLField(label="Shorten URL",
                                   required=False,
                                   widget=forms.URLInput(attrs={"class": "form-control"}))


class URLReadyForm(forms.Form):
    domains = URLDomains.objects.all()
    tinuyrl_com = URLDomains.objects.get(pk=1)

    def __init__(self, *args, **kwargs):
        super(URLReadyForm, self).__init__(*args, **kwargs)
        self.initial['domain'] = self.tinuyrl_com

    long_email = forms.URLField(label="Enter a URL to make a ShortURL",
                                required=True,
                                widget=forms.URLInput(attrs={'class': 'form-control'}))
    domain = forms.ModelChoiceField(queryset=domains, required=False,
                                    empty_label=None,
                                    label='Customize your link',
                                    widget=forms.Select(attrs={'class': 'form-control left-field',
                                                               'id': 'domain'}))
    alias = forms.CharField(min_length=5, required=False,
                            label='Alias',
                            widget=forms.TextInput(attrs={'class': 'form-control right-field',
                                                          'placeholder': 'alias',
                                                          'id': 'alias'}))
