# syntax=docker/dockerfile:1

FROM python:slim-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update; apt-get install -y python3-pip build-essential libssl-dev libffi-dev python3-dev python-dev; apt-get clean; apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt


RUN echo "SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" > .env

RUN python manage.py collectstatic --no-input; python manage.py migrate; python manage.py loaddata subjects/fixtures.json

EXPOSE 8000
CMD [ "gunicorn", "config.wsgi:application", "-b", "0.0.0.0:8000", "--log-file=-" ]
