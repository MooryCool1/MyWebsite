from Mywebsite.settings import *
import os
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['php-e4xx6g.chbkn.run']


# site framework
SITE_ID = 1


# CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://php-e4xx6g.chbkn.run', 'http://php-e4xx6g.chbkn.run']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/data/db.sqlite3',
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
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'