from django.urls import path

from .views import *

urlpatterns = [
    path('update/<str:url_username>/', update_password_view, name='update-password'),
    path('disable/<str:url_username>/', disable_tfa_view, name='disable'),
    # path('generate-lists/<str:url_username>/', generate_backup_codes, name='backup-codes'),
    path('delete-codes/<str:url_username>/', delete_codes_view, name='delete-codes'),
    path('generate-codes/<str:url_username>/', generate_backup_codes_view, name='generate-codes'),
    path('save-codes/<str:url_username>/', save_code_view, name='save-codes'),
    path('copy-codes/<str:url_username>/', copy_codes_to_clipboard_view, name='copy-codes'),
    path('generate-new-codes/<str:url_username>/', generate_new_codes_view, name='generate-new-codes'),
    path('usage/<str:url_username>/', account_usage_view, name='account_usage'),
    path('api/<str:url_username>/', generate_api_key_view, name='api-page'),
    path('api/edit/<str:token_id>/', edit_token_page_view, name='edit_token'),
    path('api/delete/<str:token_id>/', delete_token_page_view, name='delete-token')
]
