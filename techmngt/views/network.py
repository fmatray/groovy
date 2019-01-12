# coding: utf-8
"""
NetworkFlow views
"""

from django.urls import reverse_lazy

from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, \
    SingleBadgeColumn
from techmngt.forms.network import NetworkFlowForm
from techmngt.models.network import NetworkFlow


# NetworkFlow
class NetworkFlowList(BaseList):
    class NetworkFlowFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = NetworkFlow
            exclude = ['id', 'tags', 'description', 'documentation', 'comment', 'servers', 'source_nat_ip',
                       'destination_nat_ip']

    class NetworkFlowTable(BaseList.BaseTable):
        source_server = SingleBadgeColumn()
        destination_server = SingleBadgeColumn()
        view_perms = {
            "source_server": "techmngt.view_server",
            "destination_server": "techmngt.view_server",
        }

        class Meta(BaseList.BaseTable.Meta):
            model = NetworkFlow

    table_class = NetworkFlowTable
    model = NetworkFlow
    filterset_class = NetworkFlowFilter


# Detail
class NetworkFlowDetailView(BaseDetailView):
    model = NetworkFlow


# Create
class NetworkFlowCreateView(BaseCreateView):
    model = NetworkFlow
    success_message = 'Success: NetworkFlow was created.'
    form_class = NetworkFlowForm
    template_name = "techmngt/networkflow_form.html"

# Update
class NetworkFlowUpdateView(BaseUpdateView):
    model = NetworkFlow
    success_message = 'Success: NetworkFlow was updated.'
    form_class = NetworkFlowForm
    template_name = "techmngt/networkflow_form.html"


# Delete
class NetworkFlowDeleteView(BaseDeleteView):
    model = NetworkFlow
    success_message = 'Success: NetworkFlow was deleted.'
    success_url = reverse_lazy('network_list')
