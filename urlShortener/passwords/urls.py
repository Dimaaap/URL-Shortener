from django.urls import path

from .views import *


urlpatterns = [
    path('', forgot_password_view, name='forgot-password'),
    path('reset/<str:token>/', reset_password_view, name='reset-password'),
]