from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('users/', include('users.urls')),
    path('passwords/', include('passwords.urls')),
    path('account_settings/', include('account_settings.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('accounts/', include('allauth.urls'))
]

# "client_id":"908637486867-gsks371ndvuphfmgmel0soqce66q6v0m.apps.googleusercontent.com"
# "client_secret":"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",
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
