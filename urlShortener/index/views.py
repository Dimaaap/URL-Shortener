from django.shortcuts import render

from .forms import URLShortenForm


def index_page_view(request):
    if request.method == 'POST':
        form = URLShortenForm(request.POST)
    else:
        form = URLShortenForm()
    return render(request, template_name='index/index_page.html', context={'form': form})
