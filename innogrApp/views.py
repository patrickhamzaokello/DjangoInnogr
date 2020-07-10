from django.shortcuts import render
from .models import Post
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests

# Create your views here.

def basepage(request):
    return render(request, 'innogrApp/index.html')

def mydevices(request):
    return render(request,'innogrApp/pages/mydevices.html')

def newsFeed(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'innogrApp/pages/newsfeed.html', context)

def profilepage(request):
    return render(request, 'innogrApp/pages/profile/overview.html')

def Accountsettings(request):
    return render(request, 'innogrApp/pages/profile/settings.html')

def Resources(request):
    return render(request, 'innogrApp/pages/government/supportcenters.html')

def login(request):
    return render(request, 'innogrApp/pages/login.html')

def register(request):
    return render(request, 'innogrApp/pages/register.html')