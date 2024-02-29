#!/bin/ash
echo "Apply migrations"

cd "$(dirname "$0")/ciphers_project" || exit 1
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000

exec "$@"