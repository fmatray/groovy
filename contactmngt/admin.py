from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from .models import Team, Person


# Register your models here.

@admin.register(Person)
class PersonAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    fieldsets = (
        (None, {'fields': (('first_name', 'last_name'), 'title', 'team')}),
        ('Contact', {'fields': ('phone_number', 'email_address', 'web_site')}),
        ('Address', {'fields': ('street', 'city', 'province', 'postal_code', 'country')}),
        (None, {'fields': ('about', )}),
    )


@admin.register(Team)
class TeamAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'departement', 'partner')}),
        ('Contact', {'fields': ('phone_number', 'email_address', 'web_site')}),
        ('Address', {'fields': ('street', 'city', 'province', 'postal_code', 'country')}),
        (None, {'fields': ('about', )}),
    )
