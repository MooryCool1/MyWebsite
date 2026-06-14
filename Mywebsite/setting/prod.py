from Mywebsite.settings import *
import os
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['php-e4xx6g.chbkn.run', 'www.php-e4xx6g.chbkn.run']


# site framework
SITE_ID = 1


# CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://php-e4xx6g.chbkn.run', 'http://php-e4xx6g.chbkn.run']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rosalinda',
        'USER': 'postgres',
        'PASSWORD': 'jC20ouhxObKQksQ6',
        'HOST': 'services.irn6.chabokan.net',
        'PORT': '52416',
        'CONN_MAX_AGE': 600,
    }
}
STATIC_ROOT = BASE_DIR / "staticfiles"  
STATICFILES_DIRS = [
    BASE_DIR / 'statics', 
]
MEDIA_ROOT = '/var/data/media'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_KEY_PREFIX = 'mywebsite'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
        },
    },
]
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'mortezafps646@gmail.com'
PASSWORD_RESET_TIMEOUT = 86400


# Faster password hashing for low-CPU server
from django.contrib.auth.hashers import PBKDF2PasswordHasher


class FastPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    iterations = 50000


PASSWORD_HASHERS = [
    'Mywebsite.setting.prod.FastPBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]