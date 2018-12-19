# coding: utf-8

"""
Module Protocol
"""
from django.db import models
from base.models.base import Base
from model_utils import Choices

class Protocol(Base):
    TYPE = Choices('Asynchronous', 'Synchronous')
    type = models.CharField(choices=TYPE, default=TYPE.Synchronous, max_length=20)

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Protocols"