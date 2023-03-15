from django import forms


class URLShortenForm(forms.Form):
    user_email = forms.URLField(label="Your long URL",
                                widget=forms.URLInput(attrs={"class": "form-control"}))
    shorten_email = forms.URLField(label="Shorten URL",
                                   required=False,
                                   widget=forms.URLInput(attrs={"class": "form-control"}))
