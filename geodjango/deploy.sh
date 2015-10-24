#!/bin/bash
set -e
set -x
export APP_NAME=$(basename $(dirname $(find src -name settings.py -type f | head -1)))
echo "from ${APP_NAME}.settings import *" > ${BASE_DIR}/site/production.py
echo "from .base import *"               >> ${BASE_DIR}/site/production.py
echo "SECRET_KEY='"$(/usr/bin/pwgen -c -n -y 78 1)"'" >> ${BASE_DIR}/site/production.py

# Set PYTHONPATH
source ${BASE_DIR}/set_pythonpath.sh

#
# Prepare site
#
export DJANGO_SETTINGS_MODULE=site.production
/usr/bin/python src/manage.py collectstatic --link --noinput --no-color

