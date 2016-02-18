#!/bin/bash

pyenv install 3.5.0
pyenv global 3.5.0
pyenv local 3.5.0
python -m venv .pyladies
source .pyladies/bin/activate
pip install -r requirements.txt 

python manage.py test
python manage.py runserver