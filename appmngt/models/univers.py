# coding: utf-8

"""
Module univers
"""
from django.db import models
from base.models.base import Base

class Univers(Base):
    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Univers"