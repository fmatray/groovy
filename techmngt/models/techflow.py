# coding: utf-8

"""
Module Batch
"""
from django.db import models
from polymorphic.models import PolymorphicModel

from base.models.base import Base
from funcmngt.models.funcflow import SubFuncFlow


class TechFlow(Base, PolymorphicModel):
    subfunc_flow = models.OneToOneField(SubFuncFlow, on_delete=models.CASCADE, verbose_name="Functional Sub Flow",
                                        limit_choices_to={'techflow_subflow': None},
                                        default=None, blank=False, null=False, related_name="techflow_subflow")

    class Meta:
        verbose_name = 'Technical flow'