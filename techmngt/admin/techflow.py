# coding: utf-8

"""
Tech Admin
"""

from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter

from base.admin import BaseAdmin
from techmngt.models.batch import BatchFlow
from techmngt.models.techflow import TechFlow
from techmngt.models.uri import URIFlow
from techmngt.models.synchronous import SynchronousFlow


class IsVital(admin.SimpleListFilter):
    title = 'Vital'
    parameter_name = 'is_vital'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(subfunc_flow__vital=True)
        elif value == 'No':
            return queryset.filter(subfunc_flow__vital=False)
        return queryset


@admin.register(TechFlow)
class TechFlowAdmin(BaseAdmin, PolymorphicParentModelAdmin):
    """
    Admin TechFlow
    """
    base_model = TechFlow
    child_models = (BatchFlow, URIFlow, SynchronousFlow)
    fieldsets = [('Functionnal flow', {'fields': ('subfunc_flow',)}),
                 ]
    list_display = ['subfunc_flow', 'get_verbose_name', 'get_vital']
    list_filter = (PolymorphicChildModelFilter, IsVital)


class TechFlowChildAdmin(BaseAdmin, PolymorphicChildModelAdmin):
    base_model = TechFlow
