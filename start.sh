#!/bin/bash
# Startup script for Railway deployment

# Make sure we're in the right directory
cd /app

# Set Python path
export PYTHONPATH=/app:$PYTHONPATH

# Run Django migrations with error handling
echo "Running migrations..."
python manage.py migrate --noinput
MIGRATE_STATUS=$?
if [ $MIGRATE_STATUS -ne 0 ]; then
    echo "Migration failed with exit code $MIGRATE_STATUS"
    exit $MIGRATE_STATUS
fi

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput
COLLECT_STATUS=$?
if [ $COLLECT_STATUS -ne 0 ]; then
    echo "Collect static failed with exit code $COLLECT_STATUS"
    exit $COLLECT_STATUS
fi

# Start the server
echo "Starting server..."
exec gunicorn nerdhub.wsgi --log-file -