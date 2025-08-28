from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")   # কোন কোন কলাম দেখাবেন
    search_fields = ("name", "email")        # সার্চ অপশন
    list_filter = ("email",)    