# coding: utf-8

"""
Module Network
"""
from base.models import Base
from django.db import models
from model_utils import Choices

from .protocol import Protocol
from .server import Server
from .techflow import TechFlow, ServerLinkMixin


class SynchronousFlow(TechFlow, ServerLinkMixin):
    icon = "fas fa-exchange-alt"

    protocol = models.ForeignKey(Protocol, on_delete=models.PROTECT, verbose_name="Protocol",
                                 limit_choices_to={'type': 'Synchronous'},
                                 blank=False, null=False, related_name="synchronousflow_protocol")
    servers = models.ManyToManyField(Server, verbose_name="Servers",
                                     limit_choices_to=Base.LIMIT_STATUS,
                                     default=None, blank=True, related_name="sync_servers")

    identification_fields = []
    identification_list_fields = ['servers']

    class Meta(object):
        """
        meta informations
        """
        verbose_name = "Synchronous"
        verbose_name_plural = "Synchronous"
