from django.contrib import admin
from django.urls import*

app_name="blog"

from .views import*
urlpatterns = [
    path("", home, name="home"),
    path("<int:id>", single, name="single"),
]