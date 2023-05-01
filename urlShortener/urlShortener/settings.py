from pathlib import Path
import os

from decouple import config
from pythonjsonlogger.jsonlogger import JsonFormatter

from .logging_formatters import CustomJsonFormatter

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG')

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
    'account',

    'crispy_forms',
    'crispy_bootstrap5',
    'bootstrap_modal_forms',
    'debug_toolbar',
    'allauth',
    'allauth_account',
]

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth.backends.AuthenticationBackend'
]

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'APP': {
            'client-id': config('FACEBOOK_APP_ID'),
            'secret': config('FACEBOOK_APP_SECRET'),
            'key': ''
        },
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'oauth2',
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': False,
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
