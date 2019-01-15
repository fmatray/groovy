# coding: utf-8

"""
Module Network
"""
from django.db import models
from model_utils import Choices

from .techflow import TechFlow
from .protocol import Protocol

class SynchronousFlow(TechFlow):
    icon = "fas fa-exchange-alt"

    protocol = models.ForeignKey(Protocol, on_delete=models.PROTECT, verbose_name="Protocol",
                                 limit_choices_to={'status__in': ('On going', 'Released'), 'type': 'Synchronous'},
                                 blank=False, null=False, related_name="synchronousflow_protocol")

    identification_fields = []
    identification_list_fields = []
    class Meta(object):
        """
        meta informations
        """
        verbose_name = "Synchronous"
        verbose_name_plural = "Synchronous"