from django.urls import path

from .views import *


urlpatterns = [
    path('', signup_view, name='signup'),
    path('login', signin_view, name='signin'),
    path('tfa-input', tfa_input_view, name='tfa-input'),
    path('account_settings/login/facebook', facebook_login_view, name='facebook-login'),
    path('account_settings/<str:url_username>/', account_view, name='account_settings'),
    path('upload-avatar/<str:url_username>/', upload_avatar_form, name='avatar-form'),
    path('delete-account_settings/<str:url_username>/', delete_account, name='delete-account_settings'),
    path('logout', logout_users, name='logout')
]