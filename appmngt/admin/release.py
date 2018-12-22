# coding: utf-8

"""
Module de gestion de l'admin
"""
from django.contrib import admin

from appmngt.models.release import Release
from base.admin import BaseAdmin


@admin.register(Release)
class ReleaseAdmin(BaseAdmin):
    """
    Admin Release
    """
    fieldsets = [('Release', {'fields': ('release_date',)}),
                 ('Applications', {'fields': ('applications',)}), ]

    list_display = ['release_date']
    list_filter = ['applications']
    filter_horizontal = ['applications']
