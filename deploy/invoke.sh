#!/bin/bash

cd /home/app/source
pip uninstall -y south
python manage.py collectstatic --noinput
pip uninstall -y south 
python manage.py migrate
echo "Migration Ran successfully"
#NEW_RELIC_CONFIG_FILE=/scripts/newrelic.ini newrelic-admin run-program gunicorn -w 2 -b 0.0.0.0:8000 -c /scripts/config.py config.wsgi

NEW_RELIC_CONFIG_FILE=/scripts/newrelic.ini newrelic-admin run-program uwsgi /scripts/uwsgi_config.ini
