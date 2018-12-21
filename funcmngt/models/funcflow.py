# coding: utf-8

"""
Module Flow
"""
from django.db import models
from model_utils import Choices

from appmngt.models.application import Application
from base.models.base import Base


class FuncFlow(Base):
    # Choices
    type_choices = Choices('Asynchronous', 'Synchronous', 'Redirection')

    # Fields
    flow_id = models.CharField("Flow ID", max_length=64, unique=True,
                               default="", null=False, blank=False)

    type = models.CharField("Type", max_length=32, choices=type_choices)

    def __str__(self):
        return "%s (%s)" % (self.name, self.flow_id)

    class Meta:
        verbose_name = 'Functional flow'

class SubFuncFlow(Base):
    subflow_id = models.CharField("Sub flow ID", max_length=64, unique=True,
                                  default="", null=False, blank=False)
    func_flow = models.ForeignKey(FuncFlow, on_delete=models.CASCADE, verbose_name="Functional Flow",
                                 default=None, blank=True, null=True, related_name="subfuncflow_flow")
    vital = models.BooleanField("Vital", default=False)

    requester = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Requester",
                                default=None, blank=True, null=True, related_name="subfuncflow_req_app")
    receiver = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Receiver",
                                default=None, blank=True, null=True, related_name="subfuncflow_rec_app")
    class Meta:
        verbose_name = 'Sub functional flow'
