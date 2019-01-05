# coding: utf-8

"""
Module Application
"""
from django.db import models

from base.models import Base
from .partner import Partner
from .univers import Univers


class Application(Base):
    icon = "fas fa-mobile-alt"
    univers = models.ForeignKey(Univers, on_delete=models.CASCADE, verbose_name="Univers",
                                limit_choices_to = Base.LIMIT_STATUS,
                                default=None, blank=True, null=True, related_name="app_univers")
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name="Partner",
                                limit_choices_to=Base.LIMIT_STATUS,
                                default=None, blank=True, null=True, related_name="app_partner")

    identification_fields = ['univers', 'partner', 'div']
    identification_list_fields = ["env_app", "release_app", "div", "subfuncflow_req_app", "subfuncflow_rec_app"]

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "Applications"
