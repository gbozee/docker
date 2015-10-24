#!/bin/bash
# Set PYTHONPATH
source ${BASE_DIR}/set_pythonpath.sh

# Prepare DB
export DJANGO_SETTINGS_MODULE=site.production
/usr/bin/python src/manage.py migrate --noinput --no-color

# Start uwsgi
/usr/sbin/uwsgi \
    --daemonize2=${BASE_DIR}/log/uwsgi.log \
    --ini ${BASE_DIR}/site/uwsgi.ini

# Exec nginx
exec /usr/sbin/nginx -c ${BASE_DIR}/site/nginx.conf \
     -g "env base_dir=${BASE_DIR}" "$@"

