from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'innogrApp/index.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


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

