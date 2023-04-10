from django.urls import path

from .views import *


urlpatterns = [
    path('', signup_view, name='signup'),
    path('login', signin_view, name='signin'),
    path('tfa-input', tfa_input_view, name='tfa-input'),
    path('account/<str:url_username>/', account_view, name='account'),
    path('upload-avatar/<str:url_username>/', upload_avatar_form, name='avatar-form'),
    path('delete-account/<str:url_username>/', delete_account, name='delete-account'),
    path('logout', logout_users, name='logout')
]