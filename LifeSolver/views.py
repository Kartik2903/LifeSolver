
from django.shortcuts import render,redirect
from django.contrib.auth import logout

def home(req):
    return render(req, 'index.html')

# def login(req):
#     return render(req, 'accounts/login.html')



