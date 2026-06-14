#!/bin/bash
export DJANGO_SETTINGS_MODULE=Mywebsite.setting.prod
mkdir -p /var/data
mkdir -p /var/data/media
rm -rf /app/staticfiles
python manage.py migrate --noinput
python manage.py shell -c "from django.contrib.sites.models import Site; Site.objects.filter(id=1).update(domain='mooryssite.ir', name='mooryssite.ir')"
python manage.py collectstatic --noinput
python manage.py compress --force
python manage.py collectstatic --noinput
gunicorn Mywebsite.wsgi:application --bind 0.0.0.0:8000 --workers 2 --threads 2