#!/bin/bash
cd src
python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py initadmin
gunicorn --bind 0.0.0.0:8000 --workers 3 JVTimes.wsgi:application