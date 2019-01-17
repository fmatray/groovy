# coding: utf-8

"""
Module Partner
"""

from base.models import Base

class Partner(Base):
    icon = "fas fa-hands-helping"
    identification_fields = []
    identification_list_fields = ["app_partner"]

    class Meta(Base.Meta):
        """
        meta informations
        """
        verbose_name_plural = "Partners"