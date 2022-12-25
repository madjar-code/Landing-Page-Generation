from django.contrib import admin
from .models import *


@admin.register(Web)
class WebAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    ordering = ('-created_at',)
    list_display = (
        'name', 'character_code', 'is_active'
    )
    readonly_fields = ('created_at', 'updated_at', 'id')
