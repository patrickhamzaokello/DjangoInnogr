from django.shortcuts import render,redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
import requests

# Create your views here.


@login_required
def basepage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'innogrApp/index.html',context)

@login_required
def mydevices(request):
    return render(request,'innogrApp/pages/mydevices.html')

@login_required
def newsFeed(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }
    return render(request,'innogrApp/pages/newsfeed.html', context)

@login_required
def profilepage(request):
    mypost = {
        'posts': Post.objects.all()
    }
    return render(request, 'innogrApp/pages/profile/overview.html',mypost)

@login_required
def Accountsettings(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated')
            return redirect('profilepage')
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form': p_form
    }

    return render(request, 'innogrApp/pages/profile/settings.html', context)

@login_required
def Resources(request):
    return render(request, 'innogrApp/pages/government/supportcenters.html')

