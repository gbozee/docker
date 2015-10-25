#!/bin/bash
source ${BASE_DIR}/build_env.sh
echo "from ${APP_NAME}.settings import *" > ./production.py
echo "from .base import *"               >> ./production.py
echo "SECRET_KEY='"$(/usr/bin/pwgen -c -n -y 78 1| tr -d \047)"'" >> ./production.py
