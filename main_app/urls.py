# Two things to include 
# Actual path imported to settings.py

from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about' ) #views.about goes to views.py which returns render from about.html
    
]