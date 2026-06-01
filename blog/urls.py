from django.contrib import admin
from django.urls import*

app_name="blog"

from .views import*
urlpatterns = [
    path("", home, name="home"),
    path("category/<str:name>", home, name="category"),
    path("author/<str:username>", home, name="author"),

    path("<int:id>", single, name="single"),
    path("search/", search, name="search"),
]