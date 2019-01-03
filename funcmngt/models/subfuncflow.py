# coding: utf-8

"""
Module Flow
"""
from appmngt.models.application import Application
from base.models import Base
from django.db import models
from model_utils import Choices

from .funcflow import FuncFlow


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

    identification_fields = ['func_flow', 'subflow_id', 'vital']
    identification_list_fields = []

    @property
    def techflow(self):
        if self.techflow_subflow:
            return self.techflow_subflow.get_real_instance()
        return None

    class Meta:
        verbose_name = 'Sub functional flow'
