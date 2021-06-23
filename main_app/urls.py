# Two things to include 
# Actual path imported to settings.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('about/', views.about, name='about' ), #views.about goes to views.py which returns render from about.html
    path('cats/', views.cats_index, name='cats_index' ) # Get cats folder. call cats_index from views.py
    
]

# When thinking about making a webpage inside of Django
# 1. Create a view Function
# 2. Create your html page
# 3. Create a path inside of urls.py (main_app)