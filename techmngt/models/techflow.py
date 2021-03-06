# coding: utf-8

"""
Module Batch
"""
from django.db import models
from polymorphic.models import PolymorphicModel

from base.models import Base
from funcmngt.models.subfuncflow import SubFuncFlow


class TechFlow(Base, PolymorphicModel):
    icon = "fas fa-wrench"
    subfunc_flow = models.OneToOneField(SubFuncFlow, on_delete=models.PROTECT, verbose_name="Sub Functional Flow",
                                        limit_choices_to=Base.LIMIT_STATUS,
                                        default=None, blank=False, null=False, related_name="techflow_subflow")

    def get_verbose_name(self):
        return self.get_real_instance()._meta.verbose_name
    get_verbose_name.short_description = 'Type'
    get_verbose_name.empty_value_display = 'Not Available'


    def get_vital(self):
        return self.subfunc_flow.vital
    get_vital.short_description = 'Vital'
    get_vital.boolean = True

    class Meta(Base.Meta):
        verbose_name = 'Technical flow'

class ServerLinkMixin():
    pass