FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /refugio 

WORKDIR /refugio
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

COPY requirements.txt /refugio/ 

RUN pip install -r requirements.txt

COPY . /refugio/
