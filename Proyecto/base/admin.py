from django.contrib import admin
from django.utils import timezone
from .models import CustomUser

# Register your models here.
def mark_account_for_deletion(modeladmin, request, queryset):
    now = timezone.now()
    queryset.update(deleted_at=now)

mark_account_for_deletion.short_description = "Mark selected accounts for deletion"

class CustomUserAdmin(admin.ModelAdmin):
     list_display = ['username', 'email', 'first_name', 'last_name', 'get_gender_display']  # Use get_gender_display for choices

admin.site.register(CustomUser, CustomUserAdmin)