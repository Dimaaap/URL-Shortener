from django.urls import path

from .views import *

urlpatterns = [
    path('', index_page_view, name='index_page'),
    path('redirect/', redirect_into_url_view, name='redirect_view'),
    path('create-qr/', create_url_qr_png, name="create_qr"),
    path('create-qr/1200', create_url_qr_png_1200, name="create_qr_1200"),
    path('create-qr/svg', create_url_qr_svg, name='create_qr_svg')
]
