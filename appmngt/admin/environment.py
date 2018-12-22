# coding: utf-8

"""
Module de gestion de l'admin
"""
from django.contrib import admin

from appmngt.models.environment import Environment
from base.admin import BaseAdmin, BaseStackedInline


class EnvironmentInline(BaseStackedInline):
    """
    Admin  Environment
    """
    model = Environment


@admin.register(Environment)
class EnvironmentAdmin(BaseAdmin):
    """
    Admin Environment
    """
    fieldsets = [('Application', {'fields': ('application',)}),
                 ('Servers', {'fields': ('servers',)}),
                 ]
    list_display = ['application']
    filter_horizontal = ['servers']
