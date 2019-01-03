# coding: utf-8

"""
Module Network
"""
from django.db import models

from base.models import Base


class ServerType(Base):
    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Server Type"


class Server(Base):
    server_type = models.OneToOneField(ServerType, on_delete=models.CASCADE, verbose_name="Server Type",
                                       limit_choices_to=Base.LIMIT_STATUS,
                                       default=None, blank=True, null=True, related_name="server_servertype")
    dns = models.CharField("DNS", max_length=512, blank=True)
    ip = models.CharField("IP", max_length=64, blank=True)

    identification_fields = ['server_type', 'dns', 'ip']
    identification_list_fields = []
    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Servers"
