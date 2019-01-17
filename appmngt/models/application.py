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
    univers = models.ForeignKey(Univers, on_delete=models.PROTECT, verbose_name="Univers",
                                limit_choices_to = Base.LIMIT_STATUS,
                                default=None, blank=False, null=False, related_name="app_univers")
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT, verbose_name="Partner",
                                limit_choices_to=Base.LIMIT_STATUS,
                                default=None, blank=False, null=False, related_name="app_partner")

    identification_fields = ['univers', 'partner']
    identification_list_fields = ["get_envs", "get_releases", "get_subfuncflow_req_app", "get_subfuncflow_rec_app"]

    def get_envs(self):
        return self.env_app.order_by('-type')
    get_envs.verbose_name = "Environments"


    def get_releases(self):
        return self.release_app.order_by("-release_date")
    get_releases.verbose_name = "Releases"

    def get_subfuncflow_req_app(self):
        return self.subfuncflow_req_app
    get_subfuncflow_req_app.verbose_name="Sub Functional Flows as requester"

    def get_subfuncflow_rec_app(self):
        return self.subfuncflow_rec_app
    get_subfuncflow_rec_app.verbose_name="Sub Functional Flows as receiver"

    class Meta(Base.Meta):
        """
        meta informations
        """
        verbose_name_plural = "Applications"
