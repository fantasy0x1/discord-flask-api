FROM python:3.7

RUN apt update

RUN pip3 install uwsgi

COPY ./requirements.txt /srv/requirements.txt

RUN pip3 install -r /srv/requirements.txt

COPY src /srv/src
COPY server-conf /srv/server-conf

WORKDIR /srv

CMD ["/usr/local/bin/uwsgi", "--ini", "server-conf/uwsgi.ini", "--die-on-term"]
