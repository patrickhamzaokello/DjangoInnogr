from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.
context = {
        'posts': Post.objects.all()
    }

@login_required
def basepage(request):
    return render(request, 'innogrApp/index.html',context)

@login_required
def mydevices(request):
    return render(request,'innogrApp/pages/mydevices.html')

@login_required
def newsFeed(request):

    return render(request,'innogrApp/pages/newsfeed.html', context)

@login_required
def profilepage(request):
    return render(request, 'innogrApp/pages/profile/overview.html')

@login_required
def Accountsettings(request):
    return render(request, 'innogrApp/pages/profile/settings.html')

@login_required
def Resources(request):
    return render(request, 'innogrApp/pages/government/supportcenters.html')

