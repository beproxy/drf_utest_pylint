#!/bin/bash

python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput

gunicorn settings.wsgi:aplication --bind 0.0.0.0:8000

exec /bin/bash -c "$*"