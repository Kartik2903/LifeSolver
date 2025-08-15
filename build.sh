#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing Python requirements..."
pip install -r requirements.txt

echo "Collecting static files (including pre-built Tailwind CSS)..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate

echo "Build completed successfully!"
