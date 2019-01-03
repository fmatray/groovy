# coding: utf-8

"""
Module univers
"""
from base.models import Base

class Univers(Base):
    identification_fields = []
    identification_list_fields = ["app_univers"]

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Univers"