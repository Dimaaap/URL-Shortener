from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('index.urls')),
    path('users/', include('users.urls')),
    path('passwords/', include('passwords.urls')),
    path('account_settings/', include('account_settings.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('accounts/', include('allauth.urls')),
    path('dev/', include('developers.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
