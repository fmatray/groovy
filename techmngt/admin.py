# coding: utf-8

"""
Tech Admin
"""

from django.contrib import admin
from base.admin import BaseAdmin, BaseStackedInline

from .models.protocol import Protocol
from .models.network import NetworkFlow
from .models.uri import URIFlow
from .models.batch import Batch
from .models.asynchronous import AsynchronousFlow
from .models.server import Server, ServerType


@admin.register(AsynchronousFlow)
class AsynchronousFlowAdmin(BaseAdmin):
    """
    Admin AsynchronousFlow
    """
    pass



@admin.register(Batch)
class BatchAdmin(BaseAdmin):
    """
    Admin Batch
    """
    fieldsets = [('Functionnal flow', {'fields': ('subfunc_flow', )}),
                 ('Technical informations', {'fields' : (('input_flow', 'output_flow'),
                                                         'batch_name', 'ord_name','script_name')}),
                 ]
    list_display = ['subfunc_flow', 'input_flow','output_flow']

@admin.register(NetworkFlow)
class NetworkFlowAdmin(BaseAdmin):
    """
    Admin Network
    """
    fieldsets = [('Applications', {'fields': ('source_server', 'destination_server')}),
                 ('Technical informations', {'fields' : ('source_nat_ip', 'destination_nat_ip', )}),
                 ]
    list_display = ['source_server', 'source_nat_ip', 'destination_nat_ip', 'destination_server']

@admin.register(Protocol)
class ProtocolAdmin(BaseAdmin):
    """
    Admin Protocol
    """
    fieldsets = [
                 ('Technical informations', {'fields' : ('type', )}),
                 ]
    list_display = ['type']
    list_filter = ['type']


@admin.register(ServerType)
class ServerTypeAdmin(BaseAdmin):
    """
    Admin Server Type
    """
    pass

@admin.register(Server)
class ServerAdmin(BaseAdmin):
    """
    Admin Server
    """
    fieldsets = [
                 ('Technical informations', {'fields' : ('server_type', ('dns', 'ip'))}),
                 ]
    list_display = ['server_type', 'dns', 'ip']


@admin.register(URIFlow)
class URIFlowAdmin(BaseAdmin):
    """
    Admin URI
    """
    fieldsets = [('Functionnal flow', {'fields': ('subfunc_flow', )}),
                 ('Technical informations', {'fields' : ('method', 'uri')}),
                 ]