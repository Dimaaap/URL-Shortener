from django.shortcuts import render, redirect
from pyshorteners import Shortener
import qrcode
import pyperclip


from django.contrib import messages
from django.http import HttpResponse

from .forms import URLShortenForm, ShortenedURLForm
from .models import UserUrls
from .services import form_new_page_service, get_file_random_name


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
                "shorten_url": shorten_url,
                "form": ShortenedURLForm(initial={"user_url": long_url, "shorten_url": shorten_url}),
            }
            return form_new_page_service('index/new_form_template.html', new_form_context)
        else:
            # handle_form_errors = form.errors.as_text().split("*")[-1]
            messages.error(request, "Error")
    else:
        form = URLShortenForm(initial={'domain_name': 'shortenurl.com'})
        handle_form_errors = form.errors
    return render(request, 'index/main_page.html', context={'form': form
                                                            # 'form_errors': handle_form_errors
                                                            })


def redirect_into_url_view(request):
    redirect_url = request.session.get("shorten_url")
    return redirect(redirect_url)


def create_url_qr_png(request):
    shorten_url = request.session.get('shorten_url', None)
    if not shorten_url:
        return redirect(index_page_view)
    img = qrcode.make(shorten_url)
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename={get_file_random_name(1)}.png'
    img.save(response, "PNG")
    return response


def create_url_qr_png_1200(request):
    shorten_url = request.session.get('shorten_url', None)
    if not shorten_url:
        return redirect(index_page_view)
    img = qrcode.make(shorten_url, box_size=30, border=0)
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename={get_file_random_name(2)}-1200.png'
    img.save(response, 'PNG')
    return response


def create_url_qr_svg(request):
    shorten_url = request.session.get('shorten_url', None)
    if not shorten_url:
        return redirect(index_page_view)
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10, border=4)
    qr.add_data(shorten_url)
    qr.make(fit=True)
    img = qr.make_image()
    response = HttpResponse(content_type='image/svg+xml')
    response['Content-Disposition'] = f'attachment; filename={get_file_random_name(3)}.svg'
    img.save(response)
    return response


def copy_url_to_clipboard_view(request):
    shorten_url = request.session.get("shorten_url", None)
    if not shorten_url:
        messages.error(request, "Something was wrong")
    else:
        try:
            pyperclip.copy(shorten_url)
        except Exception:
            messages.error(request, "Something was wrong")
        messages.success(request, "Success Copied to clipboard")
    return redirect(index_page_view)

