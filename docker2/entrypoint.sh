#!/bin/bash

# Start MySQL service
service mysql start

# Start Django application
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
