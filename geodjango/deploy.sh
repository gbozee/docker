#!/bin/bash
export APP_NAME=$(basename $(dirname $(find src -name settings.py -type f | head -1)))
echo "from ${APP_NAME}.settings import *" >> site/production.py
echo "from .base import *" >> site/production.py
echo "SECRET_KEY='"$(/usr/bin/pwgen -c -n -y 78 1)"'" >> site/production.py
#
# Prepare site
#
export DJANGO_SETTINGS_MODULE=site.production
python src/manage.py collectstatic --link --noinput --no-color
