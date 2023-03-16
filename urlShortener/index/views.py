from django.shortcuts import render

from .forms import URLShortenForm, URLReadyForm


def index_page_view(request):
    if request.method == 'POST':
        # form = URLShortenForm(request.POST)
        form = URLReadyForm(request.POST)
    else:
        # form = URLShortenForm()
        form = URLReadyForm()
    return render(request, template_name='index/index_page.html', context={'form': form})
