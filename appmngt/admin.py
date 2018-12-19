# coding: utf-8

"""
Module de gestion de l'admin
"""
from django.contrib import admin
from django.http import HttpResponse
from base.admin import BaseAdmin, BaseStackedInline

from .models.application import Application
from .models.environment import Environment
from .models.partner import Partner
from .models.release import Release
from .models.univers import Univers


# Global
admin.site.site_header = "Ref Flux"
admin.site.site_title = "Ref Flux"
admin.site.index_title = "Bienvenue"


#  Inlines

class EnvironmentInline(BaseStackedInline):
    """
    Admin  Environment
    """

    model = Environment
    extra = 0

class ApplicationInline(BaseStackedInline):
    """
    Admin  Application
    """

    fieldsets = [('Informations', {'fields' : ('univers', 'partner')}),]

    model = Application
    extra = 0

# Admin

@admin.register(Application)
class ApplicationAdmin(BaseAdmin):
    """
    Admin Partner
    """
    fieldsets = [('Informations', {'fields' : ('univers', 'partner')}),]

    base_fields = ['univers', 'partner']

    search_fields = base_fields
    list_display = base_fields
    list_filter = base_fields
    history_list_display = base_fields
    inlines=[EnvironmentInline]



@admin.register(Environment)
class EnvironmentAdmin(BaseAdmin):
    """
    Admin Environment
    """
    fieldsets = [('Application', {'fields': ('application', )}),
                 ('Gateways', {'fields': ('gateways',)}),
                 ]
    list_display = ['application']
    filter_horizontal = ['gateways']

@admin.register(Partner)
class PartnerAdmin(BaseAdmin):
    """
    Admin Partner
    """
    inlines=[ApplicationInline]

@admin.register(Univers)
class UniversFlowAdmin(BaseAdmin):
    """
    Admin Univers
    """
    inlines=[ApplicationInline]

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
