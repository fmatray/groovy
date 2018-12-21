# coding: utf-8

"""
Module Batch
"""
from django.db import models
from model_utils import Choices

from .asynchronous import AsynchronousFlow
from .techflow import TechFlow


class BatchFlow(TechFlow):
    # Choices
    FREQUENCIES = Choices('On demand', 'On file', 'Daily', 'Weekly', 'Monthly', 'Quaterly', 'Annually')

    frequency = models.CharField("Frequency", choices=FREQUENCIES, max_length=32, blank=False, null=False)
    hours = models.CharField("Hours", max_length=256, blank=True, null=True)

    batch_name = models.CharField("Batch name", max_length=256, unique=True, default="")
    ord_name = models.CharField("Ord. name", max_length=256, unique=True, default="")
    script_name = models.CharField("Script name", max_length=256, unique=True, default="")

    input_flow = models.OneToOneField(AsynchronousFlow, on_delete=models.CASCADE, verbose_name="Input Flow",
                                      default=None, blank=True, null=True, related_name="batch_input_flow")
    output_flow = models.OneToOneField(AsynchronousFlow, on_delete=models.CASCADE, verbose_name="Output Flow",
                                       default=None, blank=True, null=True, related_name="batch_output_flow")

    class Meta:
        verbose_name = "Batch"
        verbose_name_plural = "Batches"
