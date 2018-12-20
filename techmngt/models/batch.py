# coding: utf-8

"""
Module Batch
"""
from django.db import models

from .asynchronous import AsynchronousFlow
from .techflow import TechFlow


class BatchFlow(TechFlow):
    batch_name = models.CharField("Batch name", max_length=200, unique=True, default="")
    ord_name = models.CharField("Ord. name", max_length=200, unique=True, default="")
    script_name = models.CharField("Script name", max_length=200, unique=True, default="")

    input_flow = models.OneToOneField(AsynchronousFlow, on_delete=models.CASCADE, verbose_name="Input Flow",
                                      default=None, blank=True, null=True, related_name="batch_input_flow")
    output_flow = models.OneToOneField(AsynchronousFlow, on_delete=models.CASCADE, verbose_name="Output Flow",
                                       default=None, blank=True, null=True, related_name="batch_output_flow")
