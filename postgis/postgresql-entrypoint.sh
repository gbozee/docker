#!/bin/bash
set -x
set -e
exec /usr/pgsql-${PG_VERSION}/bin/postgres \
     -D /var/lib/pgsql/${PG_VERSION}/data "$@"
