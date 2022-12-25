from django.contrib import admin
from .models import *


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    ordering = ('-created_at',)
    list_display = (
        'name', 'is_active', 'sum', 'rate',
        'minimum_term', 'maximum_term',
    )
    readonly_fields = ('created_at', 'updated_at', 'id')
