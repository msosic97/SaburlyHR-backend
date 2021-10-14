from os import name
from django.contrib.auth import login, logout
from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('newform', views.newform, name='newform'),
    path('showlist', views.showlist, name='showlist'),
    path('submitCard', views.submitCard, name='submitCard'),
    path('logout', views.logout, name='logout'),
]