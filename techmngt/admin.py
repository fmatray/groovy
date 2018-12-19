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
from .models.gateway import Gateway, GatewayCFT, GatewayWS


@admin.register(AsynchronousFlow)
class AsynchronousFlowAdmin(BaseAdmin):
    """
    Admin AsynchronousFlow
    """
    pass

@admin.register(GatewayWS)
class GatewayWSAdmin(BaseAdmin):
    """
    Admin GatewayWS
    """
    fieldsets = [
                 ('Technical informations', {'fields' : ('dns', 'protocol')}),
                 ]
    filter_horizontal= ['protocol']

@admin.register(GatewayCFT)
class GatewayCFTAdmin(BaseAdmin):
    """
    Admin GatewayCFT
    """
    fieldsets = [
                 ('Technical informations', {'fields' : ('protocol', )}),
                 ]
    filter_horizontal= ['protocol']

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
    fieldsets = [('Applications', {'fields': ('source_gateway', 'destination_gateway')}),
                 ('Technical informations', {'fields' : (('source_ip', 'source_nat_ip'),
                                                         ('destination_nat_ip', 'destination_ip'))}),
                 ]
    list_display = ['source_ip', 'source_nat_ip', 'destination_nat_ip', 'destination_ip']

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

@admin.register(URIFlow)
class URIFlowAdmin(BaseAdmin):
    """
    Admin URI
    """
    fieldsets = [('Functionnal flow', {'fields': ('subfunc_flow', )}),
                 ('Technical informations', {'fields' : ('method', 'uri')}),
                 ]