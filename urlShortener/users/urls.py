from django.urls import path

from .views import *


urlpatterns = [
    path('', signup_view, name='signup'),
    path('login', signin_view, name='signin'),
    path('account', account_view, name='account')
]