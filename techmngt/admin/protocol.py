# coding: utf-8

"""
Tech Admin
"""

from django.contrib import admin

from base.admin import BaseAdmin
from techmngt.models.protocol import Protocol


@admin.register(Protocol)
class ProtocolAdmin(BaseAdmin):
    """
    Admin Protocol
    """
    fieldsets = [
        ('Technical informations', {'fields': (('type', 'secure', 'standard'),)}),
    ]
    list_display = ['type', 'secure', 'standard']
    list_filter = ['type', 'secure', 'standard']
