FROM python:3.8.16-alpine

RUN apk update && apk upgrade
RUN apk add pkgconfig git gcc gpgme-dev libc-dev

ENV PYTHONBUFFERED 1

COPY ./. /application/.

WORKDIR /application

RUN pip3 install --upgrade pip
RUN pip3 install setuptools==30.1.0
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

EXPOSE 80/tcp
CMD gunicorn configs.wsgi:application --bind=0.0.0.0:80 --workers=4 --max-requests=1000 --timeout=1800