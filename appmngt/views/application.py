# coding: utf-8
"""
Application views
"""

from django.urls import reverse_lazy
from django_filters.filters import ModelChoiceFilter

from appmngt.forms.application import ApplicationForm
from appmngt.models.application import Application
from appmngt.models.environment import Environment
from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, \
    BadgesColumn, SingleBadgeColumn


# Application
class ApplicationList(BaseList):
    class ApplicationFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = Application

    class ApplicationTable(BaseList.BaseTable):
        univers = SingleBadgeColumn()
        partner = SingleBadgeColumn()
        env_app = BadgesColumn(verbose_name="Environments", linkify_item=True)
        release_app = BadgesColumn(verbose_name="Releases", linkify_item=True)
        subfuncflow_req_app = BadgesColumn(verbose_name="Receiver", linkify_item=True)
        subfuncflow_rec_app = BadgesColumn(verbose_name="Requester", linkify_item=True)

        view_perms = {
            'univers': 'appmngt.view_univers',
            'partner': 'appmngt.view_partner',
            'env_app': 'appmngt.view_envrionment',
            'release_app': 'appmngt.view_release',
            'subfuncflow_req_app': 'funcmngt.view_subfuncflow',
            'subfuncflow_rec_app': 'funcmngt.view_subfuncflow',
        }

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
    fields = None
    form_class = ApplicationForm
    success_message = 'Success: Application was created.'



# Update
class ApplicationUpdateView(BaseUpdateView):
    model = Application
    fields = None
    form_class = ApplicationForm
    success_message = 'Success: Application was updated.'


# Delete
class ApplicationDeleteView(BaseDeleteView):
    model = Application
    success_message = 'Success: Application was deleted.'
    success_url = reverse_lazy('application_list')
