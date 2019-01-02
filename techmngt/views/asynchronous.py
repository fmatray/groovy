# coding: utf-8
"""
AsynchronousFlow views
"""

import django_tables2 as tables
from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, \
    BadgesColumn, SingleBadgeColumn
from django.urls import reverse_lazy
from django_filters.filters import ModelChoiceFilter
from django_tables2.utils import A
from techmngt.models.asynchronous import AsynchronousFlow


# AsynchronousFlow
class AsynchronousFlowList(BaseList):
    class AsynchronousFlowFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = AsynchronousFlow
            exclude = ['id', 'tags', 'description', 'comment', 'flow_id', 'filename']

    class AsynchronousFlowTable(BaseList.BaseTable):
        batch = SingleBadgeColumn()
        view_perms = {
            'badge':'techmngt.view_batchflow'
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


# Update
class AsynchronousFlowUpdateView(BaseUpdateView):
    model = AsynchronousFlow
    success_message = 'Success: AsynchronousFlow was updated.'


# Delete
class AsynchronousFlowDeleteView(BaseDeleteView):
    model = AsynchronousFlow
    success_message = 'Success: AsynchronousFlow was deleted.'
    success_url = reverse_lazy('asynchronous_list')
