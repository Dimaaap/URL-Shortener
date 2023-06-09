from pathlib import Path
import os

from django.core.management.commands.runserver import Command as runserver
from decouple import config

from .logging_formatters import CustomJsonFormatter

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG')
runserver.default_port = '8080'

ALLOWED_HOSTS = []

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'json_formatter': {
            '()': CustomJsonFormatter,
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logs.log',
            'formatter': 'json_formatter'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'json_formatter'
        }
    },
    'loggers': {
        'users': {
            'handlers': ['file', 'console'],
            'propagate': True,
            'level': 'INFO',
        }
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'index',
    'users',
    'passwords',
    'account_settings.apps.AccountSettingsConfig',
    'developers',

    'crispy_forms',
    'crispy_bootstrap5',
    'bootstrap_modal_forms',
    'debug_toolbar',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',

    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.facebook',
]
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_JSONFIELD_ENABLED = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        "SCOPE": ['email'],
        "AUTH_PARAMS": {
            "access_type": 'online'
        },
        "APP": {
            'client_id': config('GOOGLE_CLIENT_ID'),
            'secret': config('GOOGLE_CLIENT_SECRET_KEY'),
            'key': ''
        },
        'github': {
            'SCOPE': ['user'],
            'CLIENT_ID': config('GITHUB_CLIENT_ID'),
            'SECRET': config('GITHUB_CLIENT_SECRET'),
            'USER_FIELDS': ['email', 'username'],
            'AUTH_PARAMS': {'access_type': 'online'}
        },
        'facebook': {
            'SCOPE': ['user'],
            'CLIENT_ID': config('FACEBOOK_APP_ID'),
            'SECRET': config('FACEBOOK_APP_SECRET'),
            'AUTH_PARAMS': {'access_type': 'online'}
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

AUTH_USER_MODEL = 'users.User'

SOCIAL_AUTH_GITHUB_KEY = config('GITHUB_CLIENT_ID')
SOCIAL_AUTH_GITHUB_SECRET = config('GITHUB_CLIENT_SECRET')

ROOT_URLCONF = 'urlShortener.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    #'allauth.socialaccount.backends.twitter.TwitterOAuth',
]

WSGI_APPLICATION = 'urlShortener.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT')
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kyiv'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    '127.0.0.1',
]

CRISPY_ALLOWED_TEMPLATE_PACK = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(config("EMAIL_PORT"))
EMAIL_USE_TLS = bool(config("EMAIL_USE_TLS"))

# BACKUP CODES PRE TEXT
PRE_TEXT = "SAVE YOUR BACKUP CODES\nKeep these backup codes somewhere save but accessible" \
           "\n\nLIST OF CODES:\n\n"

POST_TEXT = "\n\n*You can only use each backup code once.\n" \
            "*Need more? Visit https://url_short.com\n" \
            "*These codes were generated on"

SITE_ID = 1
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.SignUpForm'
ACCOUNT_SIGNUP_URL = '/users/'
SOCIAL_ACCOUNT_AUTO_SIGNUP = False
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
SECURE_SLL_REDIRECT = True

#CORS_SETTINGS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True