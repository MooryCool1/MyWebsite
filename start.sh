#!/bin/bash
export DJANGO_SETTINGS_MODULE=Mywebsite.setting.prod
mkdir -p /var/data
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn Mywebsite.wsgi:application --bind 0.0.0.0:8000