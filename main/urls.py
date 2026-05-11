from django.contrib import admin
from django.urls import*

app_name="main"

from .views import*
urlpatterns = [
    path("", index, name="home"),
    path("contact", contact, name="contact"),
    path("about", about, name="about"),
    path("elements", elements, name="elements"),
]