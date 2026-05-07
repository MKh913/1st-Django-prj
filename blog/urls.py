from django.contrib import admin
from django.urls import*

from .views import*
urlpatterns = [
    path("", home),
    path("single", single),
]