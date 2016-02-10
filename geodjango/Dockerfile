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
