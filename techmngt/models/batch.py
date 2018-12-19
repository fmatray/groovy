# coding: utf-8

"""
Module Batch
"""
from django.db import models
from simple_history.models import HistoricalRecords

from base.models.base import Base
from appmngt.models.environment import Environment
from appmngt.models.partner import Partner
from appmngt.models.release import Release
from funcmngt.models.funcflow import SubFuncFlow

from .asynchronous import AsynchronousFlow

class Batch(Base):
    subfunc_flow = models.ForeignKey(SubFuncFlow, on_delete=models.CASCADE, verbose_name="Functional Sub Flow",
                             default=None, blank=True, null=True, related_name="batch_subflow")

    batch_name = models.CharField("Batch name", max_length=200, unique=True, default="")
    ord_name = models.CharField("Ord. name", max_length=200, unique=True, default="")
    script_name = models.CharField("Script name", max_length=200, unique=True, default="")

    input_flow = models.OneToOneField(AsynchronousFlow, on_delete=models.CASCADE, verbose_name="Input Flow",
                                      default=None, blank=True, null=True, related_name="batch_input_flow")
    output_flow = models.OneToOneField(AsynchronousFlow, on_delete=models.CASCADE, verbose_name="Output Flow",
                                       default=None, blank=True, null=True, related_name="batch_output_flow")

    class Meta:
        ordering = ["name"]