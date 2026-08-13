# LifeSolver

A Django-based personal wellness platform with user authentication, a self-tracking dashboard, and a curated digital library. Styled with Tailwind CSS and deployed on Render.

## Features

- **User Authentication** — Signup, login, logout with Django's built-in auth system and Google OAuth (via django-allauth)
- **Dashboard** — Personal self-tracking and accountability hub
- **Digital Library** — Curated book collection fetched from Google Sheets CSV, covering topics like counselling, quizzes, and self-improvement
- **Responsive UI** — Tailwind CSS with custom styling

## Tech Stack

- **Backend**: Django 5.1, Gunicorn
- **Frontend**: HTML templates, Tailwind CSS 3
- **Auth**: django-allauth (Google OAuth), Django built-in auth
- **Deployment**: Render (with `build.sh` and `Procfile`)
- **Static Files**: WhiteNoise

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js (for Tailwind CSS build)

### Installation

```bash
# Clone the repo
git clone https://github.com/Kartik2903/LifeSolver.git
cd LifeSolver

# Install Python dependencies
pip install -r requirements.txt

# Build Tailwind CSS
npm install
npm run build

# Run migrations
python manage.py migrate

# Start the dev server
python manage.py runserver
```

Visit `http://localhost:8000`

## Project Structure

```
LifeSolver/          — Django project settings, root URLs, views
authentication/      — Signup, login, logout views
dashboard/           — User dashboard app
library/             — Book library (fetches from Google Sheets)
static/              — CSS, JS, images
templates/           — HTML templates
```

## Deployment

Deployed on [Render](https://render.com). See `Procfile` and `build.sh` for deployment configuration.

## Author

**Kartik Dewnani**

