# coding: utf-8

"""
Module Network
"""
from django.db import models
from base.models.base import Base
from model_utils import Choices

class AsynchronousFlow(Base):
    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Asynchronous Flows"