# coding: utf-8

"""
Module Environment
"""
from base.models import Base
from django.db import models
from model_utils import Choices
from techmngt.models.server import Server

from .application import Application


class Environment(Base):
    icon = "fas fa-leaf"

    TYPE = (
        ('Dev', (
            ("0", 'Dev'),
            )
        ),
        ('Project', (
            ("1", 'Integration'),
            ("2", 'Test'),
            )
        ),
        ("3", 'Pre-production'),
        ("4", 'Production'),
    )

    name = models.CharField("Name", max_length=200, blank=False, unique=False)

    type = models.CharField(choices=TYPE, max_length=10)

    application = models.ForeignKey(Application, on_delete=models.PROTECT, verbose_name="Application",
                                    limit_choices_to=Base.LIMIT_STATUS,
                                    default=None, blank=False, null=False, related_name="env_app")

    servers = models.ManyToManyField(Server, verbose_name="Servers",
                                     limit_choices_to=Base.LIMIT_STATUS,
                                     default=None, blank=True, related_name="env_servers")

    identification_fields = ['get_type', 'get_partner', 'application']
    identification_list_fields = ['servers']

    def get_type(self):
        return self.get_type_display()
    get_type.verbose_name = "Type"

    def get_partner(self):
        return self.application.partner
    get_partner.verbose_name = "Partner"

    class Meta(Base.Meta):
        """
        meta informations
        """
        verbose_name_plural = "Environments"
        unique_together = ('name', 'application')
