# coding: utf-8

"""
Module Network
"""
from django.db import models
from base.models.base import Base
from model_utils import Choices

from funcmngt.models.funcflow import SubFuncFlow


#Web Service : Method://domaine/uri

class URIFlow(Base):
    HTTP_METHOD = Choices('HEAD', 'GET', 'POST','PUT', 'DELETE')

    subfunc_flow = models.ForeignKey(SubFuncFlow, on_delete=models.CASCADE, verbose_name="Functional Sub Flow",
                                     default=None, blank=True, null=True, related_name="uri_subflow")

    uri = models.CharField("URI", max_length=512, blank=False, null=False)
    method = models.CharField("method", choices=HTTP_METHOD, max_length=32, default="")

    class Meta(object):
        """
        meta informations
        """
        verbose_name_plural = "URI Flows"