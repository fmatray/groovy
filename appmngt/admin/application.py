# coding: utf-8

"""
Module de gestion de l'admin
"""
from django.contrib import admin

from appmngt.models.application import Application
from base.admin import BaseAdmin, BaseStackedInline
from .environment import EnvironmentInline


class ApplicationInline(BaseStackedInline):
    """
    Admin  Application
    """

    fieldsets = [('Informations', {'fields': ('univers', 'partner')}), ]

    model = Application


@admin.register(Application)
class ApplicationAdmin(BaseAdmin):
    """
    Admin Partner
    """

    base_fields = ['univers', 'partner']

    search_fields = base_fields
    list_display = base_fields
    list_filter = base_fields
    history_list_display = base_fields
    inlines = [EnvironmentInline]
