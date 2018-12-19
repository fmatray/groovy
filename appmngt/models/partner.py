# coding: utf-8

"""
Module Partner
"""
from django.db import models

from base.models.base import Base

class Partner(Base):
    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Partners"