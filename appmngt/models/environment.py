# coding: utf-8

"""
Module Environment
"""
from django.db import models

from base.models import Base
from techmngt.models.server import Server
from .application import Application


class Environment(Base):
    icon = "fas fa-leaf"
    name = models.CharField("Name", max_length=200, blank=False, unique=False)

    application = models.ForeignKey(Application, on_delete=models.PROTECT, verbose_name="Application",
                                    limit_choices_to=Base.LIMIT_STATUS,
                                    default=None, blank=False, null=False, related_name="env_app")

    servers = models.ManyToManyField(Server, verbose_name="Servers",
                                     limit_choices_to=Base.LIMIT_STATUS,
                                     default=None, blank=True, related_name="env_servers")

    identification_fields = ['get_partner', 'application']
    identification_list_fields = ['servers']

    def get_partner(self):
        return self.application.partner
    get_partner.verbose_name = "Partner"

    class Meta(Base.Meta):
        """
        meta informations
        """
        verbose_name_plural = "Environments"
        unique_together = ('name', 'application')
