# coding: utf-8

"""
Module Network
"""
from django.db import models
from model_utils import Choices

from base.models.base import Base
from .protocol import Protocol


class AsynchronousFlow(Base):
    CODEPAGE = Choices('ASCII', 'Binary', 'EBCDIC')

    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE, verbose_name="Protocol",
                                 limit_choices_to={'type': 'Asynchronous'},
                                 blank=False, null=False, related_name="asynchronousflow_protocol")

    flow_id = models.CharField("Flow ID", max_length=64, unique=True, default="", null=True, blank=True)
    filename = models.CharField("File name", max_length=256, blank=True, null=True)
    codepage = models.CharField("Code page", max_length=64, choices=CODEPAGE, null=True, blank=True)

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Asynchronous Flows"
