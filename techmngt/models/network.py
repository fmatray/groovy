# coding: utf-8

"""
Module Network
"""
from django.db import models
from base.models.base import Base
from .gateway import Gateway

class NetworkFlow(Base):

    source_gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE, verbose_name="Source gateway",
                                 default=None, blank=True, null=True, related_name="source_gateway_env")
    destination_gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE, verbose_name="Destination gateway",
                                 default=None, blank=True, null=True, related_name="destination_gateway_env")


    source_ip = models.CharField("Source IP", max_length=64, blank=True)
    source_nat_ip = models.CharField("Source NAT IP", max_length=64, blank=True)

    destination_nat_ip = models.CharField("Destination NAT IP", max_length=64, blank=True)
    destination_ip = models.CharField("Destination IP", max_length=64, blank=True)


    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Network"