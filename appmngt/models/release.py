# coding: utf-8

"""
Module Release
"""
from datetime import datetime

from django.db import models

from base.models import Base
from .application import Application


class Release(Base):
    applications = models.ManyToManyField(Application, verbose_name="Applications", default=None, blank=True,
                                          related_name="release_app")

    release_date = models.DateField("Release date", blank=False, null=False, default=datetime.now)

    identification_fields = ['release_date']
    identification_list_fields = ['applications']

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Releases"