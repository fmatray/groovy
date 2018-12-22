# coding: utf-8

"""
Tech Admin
"""

from django.contrib import admin

from base.admin import BaseAdmin, BaseStackedInline
from funcmngt.models.funcflow import FuncFlow, SubFuncFlow


class SubFuncFlowInline(BaseStackedInline):
    """
    Admin sub fuctional flows
    """
    fieldsets = [('Sub flow', {'fields': ('subflow_id', 'vital')}),
                 ('Applications', {'fields': (('requester', 'receiver'),)})
                 ]
    model = SubFuncFlow


@admin.register(FuncFlow)
class FuncFlowAdmin(BaseAdmin):
    """
    Admin fuctional flows
    """
    fieldsets = [('Flow', {'fields': ('flow_id', 'type')}),
                 ]

    base_fields = ['name', 'flow_id', 'type']

    search_fields = ['type']
    list_display = base_fields
    list_filter = ['type']
    history_list_display = base_fields
    inlines = [SubFuncFlowInline]
