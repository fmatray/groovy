# coding: utf-8
"""
Server views
"""

from django.urls import reverse_lazy

from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, \
    BadgesColumn
from techmngt.forms.server import ServerForm
from techmngt.models.server import Server


# Server
class ServerList(BaseList):
    class ServerFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = Server
            exclude = ['id', 'tags','pin', 'description', 'documentation', 'comment', 'dns', 'ip']

    class ServerTable(BaseList.BaseTable):
        env_servers = BadgesColumn(verbose_name="Environment")
        view_perms = {
            'env_servers': 'appmngt.view_environment'
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
    form_class = ServerForm

# Update
class ServerUpdateView(BaseUpdateView):
    model = Server
    success_message = 'Success: Server was updated.'
    form_class = ServerForm

# Delete
class ServerDeleteView(BaseDeleteView):
    model = Server
    success_message = 'Success: Server was deleted.'
    success_url = reverse_lazy('server_list')
