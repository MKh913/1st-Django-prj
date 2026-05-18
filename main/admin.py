from django.contrib import admin
from .models import contact

# Register your models here.
class contact_admin(admin.ModelAdmin):
    date_hierarchy="created_date"
    empty_value_display="-empty-"
    list_display=("name", "email", "subject")
    list_filter=("email",)
    search_fields=["name", "subject", "message"]

admin.site.register(contact, contact_admin)