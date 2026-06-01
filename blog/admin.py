from django.contrib import admin
from .models import*

# Register your models here.
class post_admin(admin.ModelAdmin):
    date_hierarchy="created_date"
    empty_value_display="-empty-"
    list_display=("title", "author", "counted_views", "status", "published_date")
    list_filter=("status", "author")
    search_fields=["title", "content"]

admin.site.register(category)
admin.site.register(post, post_admin)