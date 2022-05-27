#!/bin/bash

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py makemigrations 
python manage.py makemigrations reserve
python manage.py migrate --noinput
python manage.py initadmin
python manage.py runserver 0.0.0.0:8000
