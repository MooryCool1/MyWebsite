from Mywebsite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!r&%%qk%#v*_lv78khn6ew2#9p%ir0^3!joll(e+9f@oe0vrc%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# site framework
SITE_ID = 3


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / "staticfiles"  
STATICFILES_DIRS = [
    BASE_DIR / 'statics', 
]
MEDIA_ROOT = BASE_DIR / 'media'

X_FRAME_OPTIONS = 'SAMEORIGIN'

EMAIL_HOST_USER = 'mortezafps646@gmail.com'
EMAIL_HOST_PASSWORD = 'oqkvtnjjhucgopyf'
DEFAULT_FROM_EMAIL = 'mortezafps646@gmail.com'