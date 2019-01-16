# coding: utf-8

"""
SynchronousFlow Admin
"""

from django.contrib import admin

from techmngt.models.synchronous import SynchronousFlow
from .techflow import TechFlowChildAdmin


@admin.register(SynchronousFlow)
class SynchronousFlowAdmin(TechFlowChildAdmin):
    """
    Admin URI
    """
    fieldsets = [('Functionnal flow', {'fields': ('subfunc_flow',)}),
                 ('Technical informations', {'fields': ('protocol', 'servers')}),
                 ]
    list_display = ['subfunc_flow']
    filter_horizontal = ['servers']
