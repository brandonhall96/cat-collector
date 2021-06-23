from django.shortcuts import render

# Create your views here.
# Methods that call upon other pages

def about(request): # Call about in our urls.py 
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')