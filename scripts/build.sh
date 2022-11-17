#!/usr/bin/env sh

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py loaddata ./subjects/fixtures/curriculums.json ./subjects/fixtures/papers.json ./subjects/fixtures/qualifications.json ./subjects/fixtures/sessions.json ./subjects/fixtures/subjects.json
