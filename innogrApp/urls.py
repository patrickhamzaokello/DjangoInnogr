from django.contrib.auth import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.basepage, name='home'),
    path('index.html', views.basepage, name='home'),
    path('myDevices', views.mydevices, name='My Devices'),
    path('newsFeed', views.newsFeed, name='My newsFeed'),
    path('Profile/Overview', views.profilepage, name='profilepage'),
    path('Profile/Settings', views.Accountsettings, name='Accountsettings'),
    path('Resources/Support', views.Resources, name='Resources'),
    path('Login', views.login, name='login'),
    path('Register', views.register, name='register'),




]