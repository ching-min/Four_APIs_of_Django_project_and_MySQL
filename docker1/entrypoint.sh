#!/bin/bash

mysql -h db -u root -p1234567 < /initdb/init.sql
exec gunicorn project.wsgi:application --bind 0.0.0.0:8000

