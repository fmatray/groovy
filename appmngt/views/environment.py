# coding: utf-8
"""
Environment views
"""
from django.urls import reverse_lazy

from appmngt.forms.environment import EnvironmentForm
from appmngt.models.environment import Environment
from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, \
    BadgesColumn, SingleBadgeColumn


# Environment

class EnvironmentMixin:
    fields = ['name', 'status', 'description', 'application', 'servers', 'comment']


class EnvironmentList(BaseList):
    class EnvironmentFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = Environment
            exclude = ['id', 'tags', 'description', 'comment', 'servers']

    class EnvironmentTable(BaseList.BaseTable):
        application = SingleBadgeColumn()
        servers = BadgesColumn(linkify_item=True)

        view_perms = {
            'application': 'appmngt.view_application',
            'servers': 'techmngt.view_server',
        }

        class Meta(BaseList.BaseTable.Meta):
            model = Environment

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
    form_class = EnvironmentForm


# Update
class EnvironmentUpdateView(BaseUpdateView):
    model = Environment
    success_message = 'Success: Environment was updated.'
    form_class = EnvironmentForm


# Delete
class EnvironmentDeleteView(BaseDeleteView):
    model = Environment
    success_message = 'Success: Environment was deleted.'
    success_url = reverse_lazy('environment_list')
