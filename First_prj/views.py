from django.shortcuts import*
from django.http import*

from templates import*

def home(request):
    return render(request, "main/home.html")

def contact(request):
    return render(request, "main/contact.html")

def about(request):
    return render(request, "main/about.html")