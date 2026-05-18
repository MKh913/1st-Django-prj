from django.contrib import admin
from .models import post

# Register your models here.
class post_admin(admin.ModelAdmin):
    date_hierarchy="created_date"
    empty_value_display="-empty-"
    list_display=("title", "counted_views", "status", "published_date")
    list_filter=("status",)
    search_fields=["title", "content"]

admin.site.register(post, post_admin)