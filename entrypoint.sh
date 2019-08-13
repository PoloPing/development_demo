#!/bin/bash
python manage.py makemigrations
until python manage.py migrate --database=default; do
  sleep 2
  echo "Retry Default!";
done
until python manage.py migrate --database=mongo; do
  sleep 2
  echo "Retry Mongo!";
done
python manage.py runserver 0.0.0.0:8000
