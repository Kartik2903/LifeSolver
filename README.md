# LifeSolver

A Django-based personal wellness platform designed around the philosophy "Seeing is Cure." Provides self-tracking tools, a curated book library with reading progress, counselling intake, self-assessment quizzes, and educational video content — all behind dual authentication (email + Google OAuth).

## Features

### Landing Page
- **Dynamic template grid** — JavaScript-rendered card layout displaying all platform modules with images, descriptions, and action buttons
- **External integrations** — Cards link to Google Sheets trackers (daily self-tracking, accountability), Google Forms (counselling booking, fun quizzes), and internal pages
- **Responsive design** — Tailwind CSS grid adapting from 1 to 2 columns across breakpoints

### Authentication
- **Dual auth system** — Two authentication paths running side-by-side:
  - **Custom auth** — Django's built-in `User` model with signup (username + email + password with confirmation), login, and logout views
  - **Google OAuth** — One-click Google sign-in via `django-allauth` with auto-signup, email-based authentication, and configurable OAuth scopes
- **Session management** — Django session middleware with CSRF protection on all forms
- **Password validation** — Django's built-in validators (similarity check, 8-char minimum, common password blocklist, numeric-only rejection)

### Book Library
- **Live Google Sheets data source** — Book catalog fetched at runtime from a published Google Sheets CSV (no local database needed)
- **Reading progress tracking** — Client-side localStorage tracks per-book state:
  - Mark as "In Progress" — records start date, shows day counter
  - Mark as "Read" — calculates and displays total reading duration in days
  - "Buy Now" — links to external purchase page
- **Color-coded status** — Cards change color based on state: red (unread), yellow (in progress), green (completed), blue (buy link clicked)

### Videos & Quizzes
- **Embedded YouTube content** — Educational videos (e.g., "What is Ego?") embedded with responsive iframe
- **Linked assessments** — Each video paired with a Google Forms quiz for self-evaluation

### Dashboard
- **Personal tracking hub** — Table-based layout for self-accountability (in development)

### Deployment
- **Render-ready** — Gunicorn WSGI server with `Procfile` and automated `build.sh` script
- **Build pipeline** — Single script handles: pip install → npm install → Tailwind CSS build → collectstatic → migrations → OAuth site setup
- **Static file serving** — WhiteNoise with `CompressedManifestStaticFilesStorage` in production
- **Environment-aware config** — Separate DEBUG/production settings, environment variables for secrets, conditional middleware loading

## Tech Stack

- **Backend**: Django 5.1, Gunicorn
- **Frontend**: Django templates, Tailwind CSS, Vanilla JavaScript
- **Auth**: django-allauth 0.57 (Google OAuth), Django built-in auth
- **Data Source**: Google Sheets (published CSV)
- **Static Files**: WhiteNoise 6.6
- **Deployment**: Render

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js (for Tailwind CSS build)

### Installation

```bash
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

### Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key |
| `ENVIRONMENT` | `development` or `production` |
| `GOOGLE_CLIENT_ID` | Google OAuth client ID |
| `GOOGLE_CLIENT_SECRET` | Google OAuth client secret |

## Project Structure

```
LifeSolver/          — Django project settings, root URLs, home view
authentication/      — Custom signup/login/logout views (email + password)
dashboard/           — Personal tracking dashboard app
library/             — Book library (fetches from Google Sheets CSV, localStorage progress)
videos/              — Educational video pages with linked quizzes
static/
├── css/             — Tailwind input/output CSS
├── script.js        — Template grid renderer with card data
├── styles.css       — Custom styles
└── images/          — Landing page card images
templates/
├── layouts/         — Base layout with nav (auth-aware)
├── account/         — AllAuth login/signup templates
├── authentication/  — Custom auth templates
├── index.html       — Landing page
├── dashboard.html   — Dashboard
└── library.html     — Book library with progress tracking
build.sh             — Automated build script for Render
Procfile             — Gunicorn process definition
```

## Author

**Kartik Dewnani**

