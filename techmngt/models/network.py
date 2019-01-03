# coding: utf-8

"""
Module Network
"""
from django.db import models

from base.models import Base
from .server import Server


class NetworkFlow(Base):

    source_server = models.ForeignKey(Server, on_delete=models.CASCADE, verbose_name="Source server",
                                 default=None, blank=True, null=True, related_name="source_server_env")
    destination_server = models.ForeignKey(Server, on_delete=models.CASCADE, verbose_name="Destination server",
                                 default=None, blank=True, null=True, related_name="destination_server_env")


    source_nat_ip = models.CharField("Source NAT IP", max_length=64, blank=True)

    destination_nat_ip = models.CharField("Destination NAT IP", max_length=64, blank=True)

    identification_fields = ['source_nat_ip', 'destination_nat_ip']
    identification_list_fields = []
    class Meta(Base.Meta):
        """
        meta informations
        """
        verbose_name = "Network flow"
        verbose_name_plural = "Network flows"
