from django.shortcuts import*
from django.http import*

from APPs_test.templates import*

#Create your views here.
def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")