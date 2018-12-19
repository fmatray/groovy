# coding: utf-8

"""
Module Network
"""
from django.db import models
from base.models.base import Base
from model_utils import Choices

from .protocol import Protocol


class Gateway(Base):
    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Gateways"

class GatewayWS(Gateway):
    dns = models.CharField("DNS", max_length=512, null=True, blank=True, default="")

    protocol = models.ManyToManyField(Protocol, limit_choices_to={'type': 'Synchronous'},
                                      verbose_name="Protocol", default=None, blank=True)


    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Gateways Web Services"

class GatewayCFT(Gateway):
    protocol = models.ManyToManyField(Protocol, limit_choices_to={'type': 'Asynchronous'},
                                      verbose_name="Protocol", default=None, blank=True)

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Gateways CFT"

