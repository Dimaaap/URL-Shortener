from django.shortcuts import render
from pyshorteners import Shortener

from .forms import URLShortenForm
from .models import UserUrls


def index_page_view(request):
    shortener = Shortener()
    user_api_address = request.META.get('REMOTE_ADDR')
    if request.method == "POST":
        form = URLShortenForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data['long_url_field']
            shorten_url = shortener.tinyurl.short(long_url)
            request.session['shorten_url'] = str(shorten_url)
            new_user_url = UserUrls.objects.create()
    else:
        form = URLShortenForm(initial={'domain_name': 'urlshort.com'})
    return render(request, 'index/main_page.html', context={'form': form})


