from django.contrib import admin
from .models import ContentManagement

class ContentManagementAdmin(admin.ModelAdmin):
    fields = ['heading', 'body', 'is_archived']
    list_display = ['heading', 'body', 'created_at', 'is_archived']

admin.site.register(ContentManagement, ContentManagementAdmin)