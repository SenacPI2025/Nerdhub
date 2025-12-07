#!/bin/bash
# Build script for Railway deployment

# Run Django migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput