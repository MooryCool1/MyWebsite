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
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neondb',
        'USER': 'neondb_owner',
        'PASSWORD': 'npg_3mcPGb8SCQHg',
        'HOST': 'ep-gentle-shadow-adw7s1bt.c-2.us-east-1.aws.neon.tech',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
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