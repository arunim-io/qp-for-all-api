# syntax=docker/dockerfile:1
FROM python:slim-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update; apt-get install -y python3-pip build-essential libssl-dev libffi-dev python3-dev python-dev
RUN apt-get clean; apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN rm -rf /root/.cache/

COPY . /app/

RUN echo "SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" > ./config/.env


EXPOSE 8000

CMD ["/bin/bash", "-c", "python manage.py collectstatic --noinput; gunicorn --bind :8000 --workers 1 --log-file=- config.wsgi:application"]
