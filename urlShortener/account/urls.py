from django.urls import path

from .views import *

urlpatterns = [
    path('update/<str:url_username>/', update_password_view, name='update-password'),
    path('disable/<str:url_username>/', disable_tfa_view, name='disable'),
    path('generate-lists/<str:url_username>/', generate_backup_codes, name='backup-codes'),
    path('delete-codes/<str:url_username>/', delete_codes_view, name='delete-codes')
]
