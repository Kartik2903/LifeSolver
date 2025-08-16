# Tailwind CSS Production Setup

## Overview
This project uses a conditional loading approach for Tailwind CSS to optimize for both development and production environments.

## Setup Details

### Development Mode (DEBUG=True)
- Uses Tailwind CDN for rapid development
- No build process required
- Loaded via: `<script src="https://cdn.tailwindcss.com"></script>`

### Production Mode (DEBUG=False)
- Uses pre-built, optimized CSS file
- Eliminates external CDN dependency for better performance and reliability
- Loaded via: `<link rel="stylesheet" href="{% static 'css/dist/styles.css' %}">`

## File Structure
```
static/
├── css/
│   └── dist/
│       └── styles.css      # Pre-built Tailwind CSS (28KB)
├── styles.css              # Custom CSS
└── ...

staticfiles/                # Collected static files for production
├── css/
│   └── dist/
│       └── styles.css      # Copied during collectstatic
└── ...
```

## Deployment Process

### 1. CSS File Preparation
The Tailwind CSS file is pre-built and copied from `theme/static/css/dist/styles.css` to `static/css/dist/styles.css`.

### 2. Build Script (build.sh)
```bash
#!/usr/bin/env bash
set -o errexit

echo "Installing Python requirements..."
pip install -r requirements.txt

echo "Collecting static files (including pre-built Tailwind CSS)..."
python manage.py collectstatic --no-input
```

### 3. Template Implementation (templates/layouts/layout.html)
```django
{% if debug %}
    <!-- Development: Use CDN for quick development -->
    <script src="https://cdn.tailwindcss.com"></script>
{% else %}
    <!-- Production: Use pre-built CSS -->
    <link rel="stylesheet" href="{% static 'css/dist/styles.css' %}">
{% endif %}
```

## Environment Configuration

### Development (.env or local settings)
```
ENVIRONMENT=development
DEBUG=True
```

### Production (Render.com environment variables)
```
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=your-secret-key
```

## Benefits

1. **Performance**: No external CDN calls in production
2. **Reliability**: CSS always available, no network dependencies
3. **Security**: Reduces external resource loading
4. **Flexibility**: Easy development with CDN, optimized production with static files
5. **Size**: Optimized CSS file (28KB vs full Tailwind framework)

## Maintenance

To update Tailwind CSS:
1. Update the pre-built CSS file in `static/css/dist/styles.css`
2. Run `python manage.py collectstatic --no-input`
3. Deploy changes

## Troubleshooting

### CSS Not Loading in Production
1. Verify `ENVIRONMENT=production` is set
2. Check that `collectstatic` was run during deployment
3. Ensure `staticfiles/css/dist/styles.css` exists
4. Verify `DEBUG=False` in production settings

### Development CSS Issues
1. Ensure `DEBUG=True` for development
2. Check internet connection for CDN access
3. Verify template conditional logic

## Files Modified
- `LifeSolver/settings.py`: Environment-based configuration
- `templates/layouts/layout.html`: Conditional CSS loading
- `static/css/dist/styles.css`: Pre-built Tailwind CSS
- `build.sh`: Deployment script with collectstatic
