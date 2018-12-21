# coding: utf-8

"""
Tech Admin
"""

from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter

from base.admin import BaseAdmin
from .models.asynchronous import AsynchronousFlow
from .models.batch import BatchFlow
from .models.network import NetworkFlow
from .models.protocol import Protocol
from .models.server import Server, ServerType
from .models.techflow import TechFlow
from .models.uri import URIFlow


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
    child_models = (BatchFlow, URIFlow)
    fieldsets = [('Functionnal flow', {'fields': ('subfunc_flow',)}),
                 ]
    list_display = ['subfunc_flow', 'get_verbose_name', 'get_vital']
    list_filter = (PolymorphicChildModelFilter, IsVital)


class TechFlowChildAdmin(BaseAdmin, PolymorphicChildModelAdmin):
    base_model = TechFlow


@admin.register(AsynchronousFlow)
class AsynchronousFlowAdmin(BaseAdmin):
    """
    Admin AsynchronousFlow
    """
    fieldsets = [('Flow', {'fields': ('flow_id', )}),
                 ('Technical informations', {'fields': (('protocol', 'codepage'), 'filename')}),
                 ]
    list_display = ['flow_id', 'protocol', 'codepage', 'filename']


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


@admin.register(NetworkFlow)
class NetworkFlowAdmin(BaseAdmin):
    """
    Admin Network
    """
    fieldsets = [('Applications', {'fields': ('source_server', 'destination_server')}),
                 ('Technical informations', {'fields': ('source_nat_ip', 'destination_nat_ip',)}),
                 ]
    list_display = ['source_server', 'source_nat_ip', 'destination_nat_ip', 'destination_server']


@admin.register(Protocol)
class ProtocolAdmin(BaseAdmin):
    """
    Admin Protocol
    """
    fieldsets = [
        ('Technical informations', {'fields': (('type', 'secure', 'standard'),)}),
    ]
    list_display = ['type', 'secure', 'standard']
    list_filter = ['type', 'secure', 'standard']


@admin.register(Server)
class ServerAdmin(BaseAdmin):
    """
    Admin Server
    """
    fieldsets = [
        ('Technical informations', {'fields': ('server_type', ('dns', 'ip'))}),
    ]
    list_display = ['server_type', 'dns', 'ip']


@admin.register(ServerType)
class ServerTypeAdmin(BaseAdmin):
    """
    Admin Server Type
    """
    pass


@admin.register(URIFlow)
class URIFlowAdmin(TechFlowChildAdmin):
    """
    Admin URI
    """
    fieldsets = [('Functionnal flow', {'fields': ('subfunc_flow',)}),
                 ('Technical informations', {'fields': ('method', 'uri')}),
                 ]
    list_display = ['subfunc_flow', 'method', 'uri']
