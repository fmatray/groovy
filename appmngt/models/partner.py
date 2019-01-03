# coding: utf-8

"""
Module Partner
"""

from base.models import Base

class Partner(Base):
    identification_fields = []
    identification_list_fields = ["app_partner"]

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Partners"