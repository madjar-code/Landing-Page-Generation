from django.contrib import admin
from .models import Template


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    ordering = ('-created_at',)
    list_display = (
        'name', 'is_active'
    )
    readonly_fields = ('created_at', 'updated_at', 'id')
