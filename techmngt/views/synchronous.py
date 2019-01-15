# coding: utf-8
"""
SynchronousFlow views
"""

import django_tables2 as tables
from django.urls import reverse_lazy

from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, \
    SingleBadgeColumn
from techmngt.forms.synchronous import SynchronousFlowForm
from techmngt.models.synchronous import SynchronousFlow


# SynchronousFlow
class SynchronousFlowList(BaseList):
    class SynchronousFlowFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = SynchronousFlow
            exclude = ['id', 'tags', 'description', 'documentation', 'comment', 'subfunc_flow',  'polymorphic_ctype']

    class SynchronousFlowTable(BaseList.BaseTable):
        get_vital = tables.BooleanColumn(verbose_name="Vital", order_by=('subfunc_flow__vital',))
        subfunc_flow = SingleBadgeColumn()

        view_perms = {
            "subfunc_flow": "funcmngt.view_subfuncflow",
        }

        class Meta(BaseList.BaseTable.Meta):
            model = SynchronousFlow
            exclude = ['id', 'description', 'documentation', 'comment', 'polymorphic_ctype', 'techflow_ptr']

    table_class = SynchronousFlowTable
    model = SynchronousFlow
    filterset_class = SynchronousFlowFilter


# Detail
class SynchronousFlowDetailView(BaseDetailView):
    model = SynchronousFlow


# Create
class SynchronousFlowCreateView(BaseCreateView):
    model = SynchronousFlow
    success_message = 'Success: SynchronousFlow was created.'
    form_class = SynchronousFlowForm
    template_name = "techmngt/synchronousflow_form.html"

# Update
class SynchronousFlowUpdateView(BaseUpdateView):
    model = SynchronousFlow
    success_message = 'Success: SynchronousFlow was updated.'
    form_class = SynchronousFlowForm
    template_name = "techmngt/synchronousflow_form.html"


# Delete
class SynchronousFlowDeleteView(BaseDeleteView):
    model = SynchronousFlow
    success_message = 'Success: SynchronousFlow was deleted.'
    success_url = reverse_lazy('synchronous_list')
