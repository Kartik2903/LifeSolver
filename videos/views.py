from django.shortcuts import render

# Create your views here.
def all_videos(req):
    return render(req, 'allvideos.html')
