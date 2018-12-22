# coding: utf-8

"""
Module de gestion de l'admin
"""
from django.contrib import admin

from appmngt.models.partner import Partner
from base.admin import BaseAdmin
from .application import ApplicationInline


@admin.register(Partner)
class PartnerAdmin(BaseAdmin):
    """
    Admin Partner
    """
    inlines = [ApplicationInline]
