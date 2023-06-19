from django.shortcuts import render
from pyshorteners import Shortener

from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string

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
            handle_form_errors = form.errors
            new_user_url = UserUrls(user_id=user_api_address, long_url=long_url, shorten_url=shorten_url)
            new_user_url.save()
            new_form_context = {
                "original_url": long_url,
                "shorten_url": shorten_url
            }
            new_form_html = render_to_string("new_form_template.html", new_form_context)
            return JsonResponse({"new_form_html": new_form_html})
        else:
            # handle_form_errors = form.errors.as_text().split("*")[-1]
            messages.error(request, "Error")
            print(form.errors)
    else:
        form = URLShortenForm(initial={'domain_name': 'urlshort.com'})
        handle_form_errors = form.errors
    return render(request, 'index/main_page.html', context={'form': form
                                                            # 'form_errors': handle_form_errors
                                                            })
