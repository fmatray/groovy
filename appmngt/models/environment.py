# coding: utf-8

"""
Module Environment
"""
from django.db import models

from base.models import Base
from techmngt.models.server import Server
from .application import Application


class Environment(Base):
    name = models.CharField("Name", max_length=200, blank=False, unique=False)

    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application",
                                    limit_choices_to=Base.LIMIT_STATUS,
                                    default=None, blank=True, null=True, related_name="env_app")

    servers = models.ManyToManyField(Server, verbose_name="Servers",
                                     limit_choices_to=Base.LIMIT_STATUS,
                                     default=None, blank=True, related_name="env_servers")

    identification_fields = ['application']
    identification_list_fields = ['servers']

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Environments"

        unique_together = ('name', 'application')
