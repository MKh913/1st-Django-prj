from django.contrib import admin
from django.urls import*

from .views import*

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("", home),
    path("contact", contact),
    path("about", about)
]