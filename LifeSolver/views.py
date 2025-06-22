
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

def home(req):
    return render(req, 'index.html')

# def login(req):
#     return render(req, 'accounts/login.html')


def setup_render_site_and_socialapp(request):
    try:
        # 1. Create site for Render
        site, created = Site.objects.get_or_create(
            domain="lifesolver.onrender.com",
            defaults={"name": "Life Solver"}
        )

        if created:
            msg1 = "✅ Site created. "
        else:
            msg1 = "ℹ️ Site already existed. "

        # 2. Link SocialApp
        app = SocialApp.objects.get(name="Google Render")
        app.sites.clear()
        app.sites.add(site)

        return HttpResponse(msg1 + "✅ SocialApp linked successfully.")
    except Exception as e:
        return HttpResponse(f"❌ Error: {e} 2")
