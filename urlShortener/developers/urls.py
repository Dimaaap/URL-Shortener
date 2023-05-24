from django.urls import path

from .views import *

urlpatterns = [
    path('doc/', documentation_view, name='developer-documentation')
]