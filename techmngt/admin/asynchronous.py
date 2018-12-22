# coding: utf-8

"""
Tech Admin
"""

from django.contrib import admin

from base.admin import BaseAdmin
from techmngt.models.asynchronous import AsynchronousFlow


@admin.register(AsynchronousFlow)
class AsynchronousFlowAdmin(BaseAdmin):
    """
    Admin AsynchronousFlow
    """
    fieldsets = [('Flow', {'fields': ('flow_id',)}),
                 ('Technical informations', {'fields': (('protocol', 'codepage'), 'filename')}),
                 ]
    list_display = ['flow_id', 'protocol', 'codepage', 'filename']
