# coding: utf-8
"""
SubFuncFlow views
"""

from django.urls import reverse_lazy

from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, \
    SingleBadgeColumn
from funcmngt.forms.subfuncflow import SubFuncFlowForm
from funcmngt.models.subfuncflow import SubFuncFlow


# SubFuncFlow

class SubFuncFlowList(BaseList):
    class SubFuncFlowFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = SubFuncFlow
            exclude = ['subflow_id', 'id','pin', 'receiver', 'requester', 'tags', 'description', 'documentation', 'comment']

    class SubFuncFlowTable(BaseList.BaseTable):
        func_flow = SingleBadgeColumn()
        techflow = SingleBadgeColumn(verbose_name="Technical flow", order_by=('techflow_subflow',))
        requester = SingleBadgeColumn()
        receiver = SingleBadgeColumn()
        view_perms = {
            "func_flow": "funcmngt.view_funcflow",
            "requester": "appmngt.view_application",
            "receiver": "appmngt.view_application"
        }

        class Meta(BaseList.BaseTable.Meta):
            model = SubFuncFlow

    table_class = SubFuncFlowTable
    model = SubFuncFlow
    filterset_class = SubFuncFlowFilter


# Detail
class SubFuncFlowDetailView(BaseDetailView):
    model = SubFuncFlow


# Create
class SubFuncFlowCreateView(BaseCreateView):
    model = SubFuncFlow
    success_message = 'Success: Sub Functional Flow was created.'
    form_class = SubFuncFlowForm
    template_name = "funcmngt/subfuncflow_form.html"

# Update
class SubFuncFlowUpdateView(BaseUpdateView):
    model = SubFuncFlow
    success_message = 'Success: Sub Functional Flow was updated.'
    form_class = SubFuncFlowForm
    template_name = "funcmngt/subfuncflow_form.html"

# Delete
class SubFuncFlowDeleteView(BaseDeleteView):
    model = SubFuncFlow
    success_message = 'Success: Sub Functional Flow was deleted.'
    success_url = reverse_lazy('subfuncflow_list')

