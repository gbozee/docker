#!/bin/bash
/usr/sbin/uwsgi --ini /srv/geodjango/site/uwsgi.ini
exec /usr/sbin/nginx -c /srv/geodjango/site/nginx.conf "$@"

