import os
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp


class Command(BaseCommand):
    help = 'Setup site and Google OAuth for production deployment'

    def handle(self, *args, **options):
        # Get environment variables
        domain = os.getenv('SITE_DOMAIN', 'lifesolver.onrender.com')
        google_client_id = os.getenv('GOOGLE_CLIENT_ID')
        google_client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
        
        # Update or create site
        site, created = Site.objects.get_or_create(
            id=1,
            defaults={'domain': domain, 'name': 'LifeSolver'}
        )
        if not created:
            site.domain = domain
            site.name = 'LifeSolver'
            site.save()
        
        self.stdout.write(
            self.style.SUCCESS(f'Site configured: {site.domain}')
        )
        
        # Setup Google OAuth if credentials are provided
        if google_client_id and google_client_secret:
            google_app, created = SocialApp.objects.get_or_create(
                provider='google',
                defaults={
                    'name': 'Google',
                    'client_id': google_client_id,
                    'secret': google_client_secret
                }
            )
            if not created:
                google_app.client_id = google_client_id
                google_app.secret = google_client_secret
                google_app.save()
            
            # Associate with site
            google_app.sites.add(site)
            
            self.stdout.write(
                self.style.SUCCESS('Google OAuth configured successfully')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Google OAuth credentials not found in environment')
            )
            self.stdout.write(
                self.style.WARNING('Set GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET environment variables')
            )
