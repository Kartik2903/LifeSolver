#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing Python requirements..."
pip install -r requirements.txt

echo "Installing Node.js dependencies..."
npm install

echo "Building Tailwind CSS..."
npm run build

echo "Collecting static files (including built Tailwind CSS)..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate

echo "Setting up OAuth and site configuration..."
python manage.py setup_oauth

echo "Build completed successfully!"
