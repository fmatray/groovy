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
                                  limit_choices_to=Base.LIMIT_STATUS,
                                  default=None, blank=True, null=True, related_name="subfuncflow_flow")
    vital = models.BooleanField("Vital", default=False)

    requester = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Requester",
                                  limit_choices_to=Base.LIMIT_STATUS,
                                  default=None, blank=True, null=True, related_name="subfuncflow_req_app")
    receiver = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Receiver",
                                 limit_choices_to=Base.LIMIT_STATUS,
                                 default=None, blank=True, null=True, related_name="subfuncflow_rec_app")

    identification_fields = ['func_flow', 'subflow_id', 'vital', 'div', 'requester_partner', 'receiver_partner']
    identification_list_fields = []

    def requester_partner(self):
        return self.requester.partner

    requester_partner.verbose_name = "Requester Partner"

    def receiver_partner(self):
        return self.receiver.partner
    receiver_partner.verbose_name = "Receiver Partner"

    @property
    def techflow(self):
        if self.techflow_subflow:
            return self.techflow_subflow.get_real_instance()
        return None

    class Meta:
        verbose_name = 'Sub functional flow'
