# coding: utf-8

"""
Tech Admin
"""

from django.contrib import admin

from techmngt.models.batch import BatchFlow
from .techflow import TechFlowChildAdmin


@admin.register(BatchFlow)
class BatchFlowAdmin(TechFlowChildAdmin):
    """
    Admin BatchFlow
    """
    fieldsets = [('Functionnal flow', {'fields': ('subfunc_flow',)}),
                 ('Start informations', {'fields': (('frequency', 'hours'),)}),
                 ('Technical informations', {'fields': (('input_flow', 'output_flow'),
                                                        'batch_name', 'ord_name', 'script_name')}),
                 ]
    list_display = ['subfunc_flow', 'input_flow', 'output_flow']
