# coding: utf-8

"""
Tech Admin
"""

from django.contrib import admin

from base.admin import BaseAdmin
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
class ServerTypeAdmin(BaseAdmin):
    """
    Admin Server Type
    """
    pass
