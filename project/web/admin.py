from django.contrib import admin, messages
from django.shortcuts import redirect
from .models import *

@admin.action(description='Сгенерировать страницу для веба')
def create_landing_page(modeladmin, request, queryset):
    messages.success(
        request, 'Сгенерирована витрина!'
    )
    return redirect('https://youtube.com/')


@admin.register(Web)
class WebAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('-created_at',)
    list_display = (
        'name', 'character_code', 'is_active'
    )
    readonly_fields = ('created_at', 'updated_at', 'id')
    actions = [create_landing_page]
    