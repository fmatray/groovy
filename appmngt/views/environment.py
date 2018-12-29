# coding: utf-8
"""
Environment views
"""
import django_tables2 as tables
from django.urls import reverse_lazy
from django_tables2.utils import A

from appmngt.forms.environment import EnvironmentModalForm
from appmngt.models.environment import Environment
from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


# Environment

class EnvironmentMixin:
    fields = ['name', 'status', 'description', 'application', 'servers', 'comment']


class EnvironmentList(BaseList):
    class EnvironmentFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = Environment

    class EnvironmentTable(BaseList.BaseTable):
        application = tables.LinkColumn(args=[A('pk')])

        class Meta(BaseList.BaseTable.Meta):
            model = Environment
            fields = ['name', 'status', 'tags', 'application']

    table_class = EnvironmentTable
    model = Environment
    filterset_class = EnvironmentFilter


# Detail
class EnvironmentDetailView(BaseDetailView):
    model = Environment


# Create
class EnvironmentCreateView(BaseCreateView):
    model = Environment
    success_message = 'Success: Environment was created.'
    form_class = EnvironmentModalForm


# Update
class EnvironmentUpdateView(BaseUpdateView):
    model = Environment
    success_message = 'Success: Environment was updated.'
    form_class = EnvironmentModalForm


# Delete
class EnvironmentDeleteView(BaseDeleteView):
    model = Environment
    success_message = 'Success: Environment was deleted.'
    success_url = reverse_lazy('environment_list')
