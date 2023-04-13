from django.urls import path

from .views import *

urlpatterns = [
    path('update/<str:url_username>/', update_password_view.as_view(), name='update-password'),
    path('disable/<str:url_username>/', disable_tfa_view, name='disable'),
    path('update/<str:url_username>/', change_device_view.as_view(), name='change-device')
]