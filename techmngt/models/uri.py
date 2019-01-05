# coding: utf-8

"""
Module Network
"""
from django.db import models
from model_utils import Choices

from .techflow import TechFlow


#Web Service : Method://domaine/uri

class URIFlow(TechFlow):
    icon = "fas fa-cloud"
    HTTP_METHOD = Choices('HEAD', 'GET', 'POST','PUT', 'DELETE')

    method = models.CharField("method", choices=HTTP_METHOD, max_length=32, default="")
    uri = models.CharField("URI", max_length=512, blank=False, null=False)

    identification_fields = ['method', 'uri']
    identification_list_fields = []
    class Meta(object):
        """
        meta informations
        """
        verbose_name = "URI"
        verbose_name_plural = "URI"