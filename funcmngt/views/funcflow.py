# coding: utf-8
"""
FuncFlow views
"""

from django.urls import reverse_lazy

from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, BadgesColumn
from funcmngt.forms.funcflow import FuncFlowForm
from funcmngt.models.funcflow import FuncFlow


# FuncFlow

class FuncFlowList(BaseList):
    class FuncFlowFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = FuncFlow
            exclude = ['id', 'flow_id', 'tags', 'description', 'documentation', 'comment']

    class FuncFlowTable(BaseList.BaseTable):
        subfuncflow_flow = BadgesColumn(verbose_name="Sub functional flows", linkify_item=True)
        view_perms = {
            'subfuncflow_flow': 'funcmngt.view_subfuncflow'
        }

        class Meta(BaseList.BaseTable.Meta):
            model = FuncFlow

    table_class = FuncFlowTable
    model = FuncFlow
    filterset_class = FuncFlowFilter


# Detail
class FuncFlowDetailView(BaseDetailView):
    model = FuncFlow


# Create
class FuncFlowCreateView(BaseCreateView):
    model = FuncFlow
    success_message = 'Success: Functional Flow was created.'
    form_class = FuncFlowForm

# Update
class FuncFlowUpdateView(BaseUpdateView):
    model = FuncFlow
    success_message = 'Success: Functional Flow was updated.'
    form_class = FuncFlowForm

# Delete
class FuncFlowDeleteView(BaseDeleteView):
    model = FuncFlow
    success_message = 'Success: Functional Flow was deleted.'
    success_url = reverse_lazy('funcflow_list')
