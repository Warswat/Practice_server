#!/bin/bash

cd /root/Practice_server/stocks_products
git pull origin master
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
deactivate
sudo systemctl restart gunicorn
