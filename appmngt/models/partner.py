# coding: utf-8

"""
Module Partner
"""

from base.models import Base

class Partner(Base):
    icon = "fas fa-hands-helping"
    identification_fields = []
    identification_list_fields = ["get_app_partner"]

    def get_app_partner(self):
        return self.app_partner
    get_app_partner.verbose_name = "Applications"

    class Meta(Base.Meta):
        """
        meta informations
        """
        verbose_name_plural = "Partners"