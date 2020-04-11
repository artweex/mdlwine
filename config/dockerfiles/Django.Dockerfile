FROM python:3.8.2-slim-buster

WORKDIR /app

COPY /config/requirements.txt /config/
COPY /config/pip.conf /etc/

RUN pip install --no-cache-dir -r /config/requirements.txt