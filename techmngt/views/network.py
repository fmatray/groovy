# coding: utf-8
"""
NetworkFlow views
"""

import django_tables2 as tables
from django.urls import reverse_lazy
from django_filters.filters import ModelChoiceFilter
from django_tables2.utils import A

from techmngt.models.network import NetworkFlow
from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, BadgesColumn, SingleBadgeColumn


# NetworkFlow
class NetworkFlowList(BaseList):
    class NetworkFlowFilter(BaseList.BaseFilter):

        class Meta(BaseList.BaseFilter.Meta):
            model = NetworkFlow
            exclude = ['id', 'tags', 'description', 'comment', 'servers', 'source_nat_ip', 'destination_nat_ip']

    class NetworkFlowTable(BaseList.BaseTable):
        view_perms = {
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


# Update
class NetworkFlowUpdateView(BaseUpdateView):
    model = NetworkFlow
    success_message = 'Success: NetworkFlow was updated.'


# Delete
class NetworkFlowDeleteView(BaseDeleteView):
    model = NetworkFlow
    success_message = 'Success: NetworkFlow was deleted.'
    success_url = reverse_lazy('network_list')
