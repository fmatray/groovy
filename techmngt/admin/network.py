# coding: utf-8

"""
Tech Admin
"""

from django.contrib import admin

from base.admin import BaseAdmin
from techmngt.models.network import NetworkFlow


@admin.register(NetworkFlow)
class NetworkFlowAdmin(BaseAdmin):
    """
    Admin Network
    """
    fieldsets = [('Applications', {'fields': ('source_server', 'destination_server')}),
                 ('Technical informations', {'fields': ('source_nat_ip', 'destination_nat_ip',)}),
                 ]
    list_display = ['source_server', 'source_nat_ip', 'destination_nat_ip', 'destination_server']
