#!/bin/bash

virtualenv --python=python3 .pyladies
source .pyladies/bin/activate
pip install -r requirements.txt 

python manage.py test
python manage.py runserver