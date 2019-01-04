# coding: utf-8

"""
Module Network
"""
from base.models import Base
from django.db import models

from .server import Server


class NetworkFlow(Base):
    source_server = models.ForeignKey(Server, on_delete=models.CASCADE, verbose_name="Source server",
                                      limit_choices_to=Base.LIMIT_STATUS,
                                      default=None, blank=True, null=True, related_name="source_server_env")
    destination_server = models.ForeignKey(Server, on_delete=models.CASCADE, verbose_name="Destination server",
                                           limit_choices_to=Base.LIMIT_STATUS,
                                           default=None, blank=True, null=True, related_name="destination_server_env")

    source_nat_ip = models.CharField("Source NAT IP", max_length=64, blank=True)

    destination_nat_ip = models.CharField("Destination NAT IP", max_length=64, blank=True)

    identification_fields = ['source_server_ip', 'source_nat_ip', 'destination_nat_ip', 'destination_server_ip']
    identification_list_fields = []

    def source_server_ip(self):
        try:
            return self.source_server.ip
        except NameError:
            return None
    source_server_ip.verbose_name = "Source Server IP"

    def destination_server_ip(self):
        try:
            return self.destination_server.ip
        except NameError:
            return None

    destination_server_ip.verbose_name = "Destination Server IP"

    class Meta(Base.Meta):
        """
        meta informations
        """
        verbose_name = "Network flow"
        verbose_name_plural = "Network flows"
