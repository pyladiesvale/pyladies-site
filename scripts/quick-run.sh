#!/bin/bash

source .pyladies/bin/activate

python manage.py test
python manage.py runserver