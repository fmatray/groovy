# coding: utf-8

"""
Module Application
"""
from django.db import models

from base.models import Base
from .partner import Partner
from .univers import Univers


class Application(Base):
    univers = models.ForeignKey(Univers, on_delete=models.CASCADE, verbose_name="Univers",
                                     default=None, blank=True, null=True, related_name="app_univers")
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name="Partner",
                                default=None, blank=True, null=True, related_name="app_partner")

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Applications"