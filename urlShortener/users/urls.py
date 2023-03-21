from django.urls import path

from .views import *


urlpatterns = [
    path('', signup_view, name='signup'),
    path('login', signin_view, name='signin')
]