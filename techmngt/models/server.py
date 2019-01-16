# coding: utf-8

"""
Module Network
"""
from base.models import Base, BaseConfig
from django.db import models


class ServerType(BaseConfig):
    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Server Type"


class Server(Base):
    icon = "fas fa-server"
    server_type = models.ForeignKey(ServerType, on_delete=models.PROTECT, verbose_name="Server Type",
                                    default=None, blank=False, null=False, related_name="server_servertype")
    dns = models.CharField("DNS", max_length=512, blank=True)
    ip = models.CharField("IP", max_length=64, blank=True)

    identification_fields = ['server_type', 'dns', 'ip']
    identification_list_fields = []

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Servers"
