# coding: utf-8

"""
Module Network
"""
from django.db import models

from base.models.base import Base


class ServerType(Base):
    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Server Type"


class Server(Base):
    dns = models.CharField("DNS", max_length=512, blank=True)
    ip = models.CharField("IP", max_length=64, blank=True)
    server_type = models.OneToOneField(ServerType, on_delete=models.CASCADE, verbose_name="Server Type",
                                       default=None, blank=True, null=True, related_name="server_servertype")

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Servers"
