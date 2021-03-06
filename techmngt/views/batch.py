# coding: utf-8
"""
BatchFlow views
"""

import django_tables2 as tables
from django.urls import reverse_lazy

from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, \
    SingleBadgeColumn
from techmngt.forms.batch import BatchFlowForm
from techmngt.models.batch import BatchFlow


# BatchFlow
class BatchFlowList(BaseList):
    class BatchFlowFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = BatchFlow
            exclude = ['id', 'tags', 'description','pin', 'documentation', 'comment', 'hours', 'batch_name', 'ord_name',
                       'script_name', 'subfunc_flow', 'input_flow', 'input_flow', 'polymorphic_ctype']

    class BatchFlowTable(BaseList.BaseTable):
        get_vital = tables.BooleanColumn(verbose_name="Vital", order_by=('subfunc_flow__vital', ))
        subfunc_flow = SingleBadgeColumn()
        input_flow = SingleBadgeColumn()
        output_flow = SingleBadgeColumn()

        view_perms = {
            "subfunc_flow": "funcmngt.view_subfuncflow",
            "input_flow": "techmngt.view_asynchronousflow",
            "output_flow": "techmngt.view_asynchronousflow"
        }

        class Meta(BaseList.BaseTable.Meta):
            model = BatchFlow
            exclude = ['id', 'description','pin', 'documentation', 'comment', 'polymorphic_ctype', 'techflow_ptr']

    table_class = BatchFlowTable
    model = BatchFlow
    filterset_class = BatchFlowFilter


# Detail
class BatchFlowDetailView(BaseDetailView):
    model = BatchFlow


# Create
class BatchFlowCreateView(BaseCreateView):
    model = BatchFlow
    success_message = 'Success: BatchFlow was created.'
    form_class = BatchFlowForm
    template_name = "techmngt/batchflow_form.html"

# Update
class BatchFlowUpdateView(BaseUpdateView):
    model = BatchFlow
    success_message = 'Success: BatchFlow was updated.'
    form_class = BatchFlowForm
    template_name = "techmngt/batchflow_form.html"

# Delete
class BatchFlowDeleteView(BaseDeleteView):
    model = BatchFlow
    success_message = 'Success: BatchFlow was deleted.'
    success_url = reverse_lazy('batch_list')
