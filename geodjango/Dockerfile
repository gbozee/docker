FROM centos:7

ENV CENTOS_VERSION=7 \
    PG_VERSION=9.4 \
    PG_NODOT=94 \
    POSTGIS_VERSION=2 \
    BASE_DIR=/srv/geodjango

RUN cd /tmp && \
    yum install -y epel-release && \
    curl -o pgdg.rpm http://yum.postgresql.org/${PG_VERSION}/redhat/rhel-${CENTOS_VERSION}-x86_64/pgdg-redhat${PG_NODOT}-${PG_VERSION}-1.noarch.rpm && \
    yum localinstall -y pgdg.rpm && \
    yum upgrade -y && \
    yum install -y \
        GeoIP-devel \
        GeoIP-update \
        gdal \
        gdal-devel \
        geos \
        geos-devel \
        nginx \
        postgresql${PG_NODOT} \        
        postgresql${PG_NODOT}-devel \        
        proj-devel \
        pwgen \
        python-pip \
        python-virtualenv \
        uwsgi-plugin-python

RUN mkdir -pv ${BASE_DIR}/src && \
    mkdir -pv ${BASE_DIR}/site && \
    mkdir -pv ${BASE_DIR}/log

COPY site ${BASE_DIR}/site
COPY deploy.sh ${BASE_DIR}/deploy.sh

WORKDIR ${BASE_DIR}

ENV PIP /usr/bin/pip install --no-cache-dir
ENV PATH /usr/pgsql-${PG_VERSION}/bin:${PATH}

ONBUILD COPY . ${BASE_DIR}/src
ONBUILD RUN ${PIP} --no-cache-dir --upgrade pip
ONBUILD RUN ${PIP} -r $(find . -type f -name requirements.txt| head -1)
ONBUILD RUN ./deploy.sh

VOLUME ${BASE_DIR}