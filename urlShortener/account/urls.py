from django.urls import path

from .views import *

urlpatterns = [
    path('update/<str:url_username>/', update_password_view, name='update-password'),
    #path('update/<str:url_username>/', input_code_form_view, name='input-code'),
]