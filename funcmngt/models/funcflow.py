# coding: utf-8

"""
Module Flow
"""
from django.db import models
from model_utils import Choices

from base.models import Base


class FuncFlow(Base):
    # Choices
    type_choices = Choices('Asynchronous', 'Synchronous', 'Redirection')

    # Fields
    flow_id = models.CharField("Flow ID", max_length=64, unique=True,
                               default="", null=False, blank=False)

    type = models.CharField("Type", max_length=32, choices=type_choices)

    identification_fields = ['flow_id', 'type']
    identification_list_fields = ['subfuncflow_flow']

    class Meta:
        verbose_name = 'Functional flow'
