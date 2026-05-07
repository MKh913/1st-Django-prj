from django.contrib import admin
from django.urls import*

from .views import*

urlpatterns = [
    path("", index),
    path("contact", contact),
    path("about", about),
]