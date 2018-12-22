# coding: utf-8

"""
Tech Admin
"""

from django.contrib import admin

from techmngt.models.uri import URIFlow
from .techflow import TechFlowChildAdmin


@admin.register(URIFlow)
class URIFlowAdmin(TechFlowChildAdmin):
    """
    Admin URI
    """
    fieldsets = [('Functionnal flow', {'fields': ('subfunc_flow',)}),
                 ('Technical informations', {'fields': ('method', 'uri')}),
                 ]
    list_display = ['subfunc_flow', 'method', 'uri']
