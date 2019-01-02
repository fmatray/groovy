# coding: utf-8
"""
URIFlow views
"""

import django_tables2 as tables
from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, \
    BadgesColumn, SingleBadgeColumn
from django.urls import reverse_lazy
from django_filters.filters import ModelChoiceFilter
from django_tables2.utils import A
from techmngt.models.uri import URIFlow


# URIFlow
class URIFlowList(BaseList):
    class URIFlowFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = URIFlow
            exclude = ['id', 'tags', 'description', 'comment', 'subfunc_flow',  'polymorphic_ctype', 'uri']

    class URIFlowTable(BaseList.BaseTable):
        get_vital = tables.BooleanColumn(verbose_name="Vital", order_by=('subfunc_flow__vital',))
        subfunc_flow = SingleBadgeColumn()

        view_perms = {
            "subfunc_flow": "funcmngt.view_subfuncflow",
        }

        class Meta(BaseList.BaseTable.Meta):
            model = URIFlow
            exclude = ['id', 'tags', 'description', 'comment', 'polymorphic_ctype', 'techflow_ptr']

    table_class = URIFlowTable
    model = URIFlow
    filterset_class = URIFlowFilter


# Detail
class URIFlowDetailView(BaseDetailView):
    model = URIFlow


# Create
class URIFlowCreateView(BaseCreateView):
    model = URIFlow
    success_message = 'Success: URIFlow was created.'


# Update
class URIFlowUpdateView(BaseUpdateView):
    model = URIFlow
    success_message = 'Success: URIFlow was updated.'


# Delete
class URIFlowDeleteView(BaseDeleteView):
    model = URIFlow
    success_message = 'Success: URIFlow was deleted.'
    success_url = reverse_lazy('uri_list')
