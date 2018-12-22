# coding: utf-8

"""
Module Environment
"""
from django.db import models

from base.models import Base
from techmngt.models.server import Server
from .application import Application


class Environment(Base):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application",
                                     default=None, blank=True, null=True, related_name="env_app")

    servers = models.ManyToManyField(Server, verbose_name="Servers",
                                     default=None, blank=True, related_name="env_servers")


    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Environments"