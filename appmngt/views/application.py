# coding: utf-8
"""
Application views
"""

import django_tables2 as tables
from django.urls import reverse_lazy
from django_tables2.utils import A

from appmngt.forms.application import ApplicationModalForm
from appmngt.models.application import Application
from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


# Application

class ApplicationMixin:
    fields = ['name', 'status', 'description', 'univers', 'partner', 'comment']


class ApplicationList(BaseList):
    class ApplicationFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = Application
            fields = ['univers', 'partner']

    class ApplicationTable(BaseList.BaseTable):
        univers = tables.LinkColumn(args=[A('pk')])
        partner = tables.LinkColumn(args=[A('pk')])
        env_app = tables.ManyToManyColumn(verbose_name="Environments", linkify_item=True)
        release_app = tables.ManyToManyColumn(verbose_name="Releases", linkify_item=True)
        subfuncflow_req_app = tables.ManyToManyColumn(verbose_name="Receiver", linkify_item=True)
        subfuncflow_rec_app = tables.ManyToManyColumn(verbose_name="Requester", linkify_item=True)

        class Meta(BaseList.BaseTable.Meta):
            model = Application

    table_class = ApplicationTable
    model = Application
    filterset_class = ApplicationFilter


# Detail
class ApplicationDetailView(BaseDetailView):
    model = Application


# Create
class ApplicationCreateView(BaseCreateView):
    model = Application
    success_message = 'Success: Application was created.'
    form_class = ApplicationModalForm


# Update
class ApplicationUpdateView(BaseUpdateView):
    model = Application
    success_message = 'Success: Application was updated.'
    form_class = ApplicationModalForm


# Delete
class ApplicationDeleteView(BaseDeleteView):
    model = Application
    success_message = 'Success: Application was deleted.'
    success_url = reverse_lazy('application_list')
