from django.shortcuts import render

# Create your views here.
from templates import*

def index(request):
    return render(request, "main/index.html")

def contact(request):
    return render(request, "main/contact.html")

def about(request):
    return render(request, "main/about.html")

