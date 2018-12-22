# coding: utf-8

"""
Module Protocol
"""
from django.db import models
from model_utils import Choices

from base.models import Base


class Protocol(Base):
    TYPE = Choices('Asynchronous', 'Synchronous')
    type = models.CharField(choices=TYPE, default=TYPE.Synchronous, max_length=20)

    secure = models.BooleanField("Secure", default=False)
    standard = models.BooleanField("Standard", default=False)

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Protocols"
