from django.shortcuts import render
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests

# Create your views here.


def basepage(request):
    return render(request, 'base.html')

def aboutpage(request):
    return render(request, 'about.html')

def widgets(request):
    return render(request, 'pages/widgets.html')