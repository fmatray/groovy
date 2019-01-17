# coding: utf-8
"""
AsynchronousFlow views
"""

from django.urls import reverse_lazy

from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, \
    SingleBadgeColumn
from techmngt.forms.asynchronous import AsynchronousFlowForm
from techmngt.models.asynchronous import AsynchronousFlow


# AsynchronousFlow
class AsynchronousFlowList(BaseList):
    class AsynchronousFlowFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = AsynchronousFlow
            exclude = ['id', 'tags','pin', 'description', 'documentation', 'comment', 'flow_id', 'filename']

    class AsynchronousFlowTable(BaseList.BaseTable):
        batch = SingleBadgeColumn()
        view_perms = {
            'batch':'techmngt.view_batchflow'
        }
        class Meta(BaseList.BaseTable.Meta):
            model = AsynchronousFlow

    table_class = AsynchronousFlowTable
    model = AsynchronousFlow
    filterset_class = AsynchronousFlowFilter


# Detail
class AsynchronousFlowDetailView(BaseDetailView):
    model = AsynchronousFlow


# Create
class AsynchronousFlowCreateView(BaseCreateView):
    model = AsynchronousFlow
    success_message = 'Success: AsynchronousFlow was created.'
    form_class = AsynchronousFlowForm
    template_name = "techmngt/asynchronousflow_form.html"

# Update
class AsynchronousFlowUpdateView(BaseUpdateView):
    model = AsynchronousFlow
    success_message = 'Success: AsynchronousFlow was updated.'
    form_class = AsynchronousFlowForm
    template_name = "techmngt/asynchronousflow_form.html"

# Delete
class AsynchronousFlowDeleteView(BaseDeleteView):
    model = AsynchronousFlow
    success_message = 'Success: AsynchronousFlow was deleted.'
    success_url = reverse_lazy('asynchronous_list')
