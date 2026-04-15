from django.contrib import admin
from django.urls import*

from .views import*

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("HTTP test", http_test),
    path("JSON test", json_test)
]