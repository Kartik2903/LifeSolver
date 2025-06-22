
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

def home(req):
    return render(req, 'index.html')

# def login(req):
#     return render(req, 'accounts/login.html')

def fix_render_google_site_link(request):
    try:
        site = Site.objects.get(domain="lifesolver.onrender.com")
        app = SocialApp.objects.get(name="Google Render")
        app.sites.clear()
        app.sites.add(site)
        return HttpResponse("✅ SocialApp linked to correct site.")
    except Exception as e:
        return HttpResponse(f"❌ Error: {e}")

