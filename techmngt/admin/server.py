# coding: utf-8

"""
Tech Admin
"""

from base.admin import BaseAdmin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin
from techmngt.models.server import Server, ServerType


@admin.register(Server)
class ServerAdmin(BaseAdmin):
    """
    Admin Server
    """
    fieldsets = [
        ('Technical informations', {'fields': ('server_type', ('dns', 'ip'))}),
    ]
    list_display = ['server_type', 'dns', 'ip']


@admin.register(ServerType)
class ServerTypeAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    """
    Admin ServerType
    """
    pass