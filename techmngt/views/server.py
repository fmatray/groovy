# coding: utf-8
"""
Server views
"""

import django_tables2 as tables
from django.urls import reverse_lazy
from django_filters.filters import ModelChoiceFilter
from django_tables2.utils import A

from techmngt.models.server import Server
from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, BadgesColumn, SingleBadgeColumn


# Server
class ServerList(BaseList):
    class ServerFilter(BaseList.BaseFilter):

        class Meta(BaseList.BaseFilter.Meta):
            model = Server

    class ServerTable(BaseList.BaseTable):

        view_perms = {

        }

        class Meta(BaseList.BaseTable.Meta):
            model = Server

    table_class = ServerTable
    model = Server
    filterset_class = ServerFilter


# Detail
class ServerDetailView(BaseDetailView):
    model = Server


# Create
class ServerCreateView(BaseCreateView):
    model = Server
    success_message = 'Success: Server was created.'


# Update
class ServerUpdateView(BaseUpdateView):
    model = Server
    success_message = 'Success: Server was updated.'


# Delete
class ServerDeleteView(BaseDeleteView):
    model = Server
    success_message = 'Success: Server was deleted.'
    success_url = reverse_lazy('server_list')
