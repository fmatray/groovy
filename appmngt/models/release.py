# coding: utf-8

"""
Module Release
"""
from datetime import datetime
from django.db import models

from base.models.base import Base
from .application import Application

class Release(Base):
    applications = models.ManyToManyField(Application,
                                          verbose_name="Application", default=None, blank=True)

    release_date = models.DateField("Release date", blank=False, null=False, default=datetime.now)

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Releases"