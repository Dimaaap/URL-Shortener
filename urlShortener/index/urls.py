from django.urls import path

from .views import *

urlpatterns = [
    path('', index_page_view, name='index_page')
]
