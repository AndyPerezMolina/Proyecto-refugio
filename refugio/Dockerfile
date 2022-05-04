FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
    && apk add libffi-dev py-cffi \
    && apk add gettext \
    && apk add postgresql-client

RUN mkdir /refugio 

WORKDIR /refugio

COPY requirements.txt /refugio/ 

RUN pip install -r requirements.txt

COPY . /refugio/
