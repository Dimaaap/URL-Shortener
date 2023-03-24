from django.urls import path

from .views import *


urlpatterns = [
    path('', signup_view, name='signup'),
    path('login', signin_view, name='signin'),
    path('account/<str:url_username>/', account_view, name='account'),
    path('upload-avatar/<str:url_username>/', upload_avatar_form, name='avatar-form')
]