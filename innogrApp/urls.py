from django.contrib.auth import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.basepage, name='blog-home'),
    path('index.html', views.basepage, name='home'),
    path('myDevices', views.mydevices, name='MyDevices'),
    path('newsFeed', views.newsFeed, name='MynewsFeed'),
    path('Profile/Overview', views.profilepage, name='profilepage'),
    path('Profile/Settings', views.Accountsettings, name='Accountsettings'),
    path('Resources/Support', views.Resources, name='Resources'),


]