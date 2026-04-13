#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Create the media products directory if it evaporates on deploy
mkdir -p media/products
# Seed the database with products and admin (safe since it checks if they exist)
python init_db.py
