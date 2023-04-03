from django.urls import path

from .views import *

urlpatterns = [
    path('update/<str:url_username>/', update_password_view, name='update-password'),
    path('tfa-enable/<str:url_username>/', tfa_enable_view, name='tfa-enable')
]