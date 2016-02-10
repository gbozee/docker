<<<<<<< HEAD
FROM python:2.7
MAINTAINER Olivier Tabone <olivier.tabone@ripplemotion.fr>

ENV C_INCLUDE_PATH /usr/include/gdal/
ENV CPLUS_INCLUDE_PATH /usr/include/gdal/

RUN set -x \
    && apt-get update \
    && apt-get install -y \
        libgdal-dev \
        swig \
        postgresql-client \
        protobuf-compiler \
        libprotoc-dev \
        locales \
        osmosis \
        libgeoip-dev geoip-database-extra \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
       

RUN set -x \
    && mkdir -p ~/.ssh \
    && ssh-keyscan -t rsa bitbucket.org > ~/.ssh/known_hosts \
    && chmod 644 ~/.ssh/known_hosts

RUN set -x \
   && pip install --upgrade pip virtualenv setuptools wheel

=======
FROM ripplemotion/geodjango-box
MAINTAINER Biola Oyeniyi <gbozee@gmail.com>

RUN mkdir -p /home/app/source /scripts

COPY vicinity/ /home/app/source
RUN pip install -r /home/app/source/requirements.txt
COPY deploy/invoke.sh /scripts/
COPY deploy/config.py /scripts/
COPY deploy/newrelic.ini /scripts/
COPY deploy/uwsgi_config.ini /scripts/

RUN chmod +x /scripts/invoke.sh

WORKDIR /home/app/source

RUN mkdir -p /var/tuteria && mkdir -p /var/tuteria_media && usermod -a -G www-data app && chgrp -R www-data /var/tuteria && chmod -R g+w /var/tuteria && chgrp -R www-data /var/tuteria_media && chmod -R g+w /var/tuteria_media

VOLUME ["/tmp","/var/tuteria","/var/tuteria_media"]
# run startup scripts which copies staticfiles, run migration and starts server
CMD ["/scripts/invoke.sh"]

EXPOSE 8000
>>>>>>> 40bab65b2b3ec9d5e0aa0d8c11497b89de9f0619
