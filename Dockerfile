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

RUN mkdir -p /var/tuteria && mkdir -p /var/tuteria_media && chgrp -R www-data /var/tuteria && chmod -R g+w /var/tuteria && chgrp -R www-data /var/tuteria_media
VOLUME ["/tmp","/var/tuteria","/var/tuteria_media"]
# run startup scripts which copies staticfiles, run migration and starts server
CMD ["/scripts/invoke.sh"]

EXPOSE 8000
