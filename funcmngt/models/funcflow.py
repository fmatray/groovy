# coding: utf-8

"""
Module Flow
"""
from django.db import models
from model_utils import Choices

from base.models import Base


class FuncFlow(Base):
    icon = "fas fa-stream"
    # Choices
    type_choices = Choices('Asynchronous', 'Synchronous', 'Redirection')

    # Fields
    flow_id = models.CharField("Flow ID", max_length=64, unique=True,
                               default="", null=False, blank=False)

    type = models.CharField("Type", max_length=32, choices=type_choices)

    identification_fields = ['flow_id', 'type']
    identification_list_fields = ['get_subfuncflow_flow']

    def get_subfuncflow_flow(self):
        return self.subfuncflow_flow
    get_subfuncflow_flow.verbose_name = "Sub functional flows"

    class Meta(Base.Meta):
        verbose_name = 'Functional flow'
