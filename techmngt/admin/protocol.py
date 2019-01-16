# coding: utf-8

"""
Tech Admin
"""

from base.admin import BaseAdmin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin
from techmngt.models.protocol import Protocol


@admin.register(Protocol)
class ProtocolAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    """
    Admin Protocol
    """
    fieldsets = [
        ('Technical informations', {'fields': (('type', 'secure', 'standard'),)}),
    ]
    list_display = ['type', 'secure', 'standard']
    list_filter = ['type', 'secure', 'standard']
