# coding: utf-8

"""
Module de gestion de l'admin
"""
from django.contrib import admin

from appmngt.models.univers import Univers
from base.admin import BaseAdmin
from .application import ApplicationInline


@admin.register(Univers)
class UniversFlowAdmin(BaseAdmin):
    """
    Admin Univers
    """
    inlines = [ApplicationInline]
