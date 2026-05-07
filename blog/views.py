from django.shortcuts import render

# Create your views here.
from templates import*

def home(request):
    return render(request, "blog/home.html")

def single(request):
    return render(request, "blog/single.html")