#!/bin/bash
# Startup script for Railway deployment

# Run Django migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the server
echo "Starting server..."
exec gunicorn nerdhub.wsgi --log-file -