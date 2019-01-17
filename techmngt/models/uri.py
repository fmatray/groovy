# coding: utf-8

"""
Module URI
"""
from base.models import Base
from django.db import models
from model_utils import Choices

from .server import Server
from .techflow import TechFlow, ServerLinkMixin


# Web Service : Method://domaine/uri

class URIFlow(TechFlow, ServerLinkMixin):
    icon = "fas fa-cloud"
    HTTP_METHOD = Choices('HEAD', 'GET', 'POST', 'PUT', 'DELETE')

    method = models.CharField("method", choices=HTTP_METHOD, max_length=32, default="")
    uri = models.CharField("URI", max_length=512, blank=False, null=False)

    servers = models.ManyToManyField(Server, verbose_name="Servers",
                                     limit_choices_to=Base.LIMIT_STATUS,
                                     default=None, blank=True, related_name="uri_servers")

    identification_fields = ['method', 'uri']
    identification_list_fields = ['servers']

    def get_all_uris(self):
        return ["{}{}".format(server.dns, self.uri) for server in self.servers.all() ]
    get_all_uris.verbose_name = "All URIs"

    class Meta(Base.Meta):
        """
        meta informations
        """
        verbose_name = "URI"
        verbose_name_plural = "URI"
