from django.shortcuts import render
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests

# Create your views here.


def basepage(request):
    return render(request, 'index.html')

def mydevices(request):
    return render(request,'pages/mydevices.html')

def newsFeed(request):
    return render(request,'pages/newsfeed.html')

def profilepage(request):
    return render(request, 'pages/profile/overview.html')

def Accountsettings(request):
    return render(request, 'pages/profile/settings.html')

def Resources(request):
    return render(request, 'pages/government/supportcenters.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')