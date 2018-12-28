# coding: utf-8
"""
Application views
"""
from django.urls import reverse_lazy

from appmngt.forms.application import ApplicationModalForm
from appmngt.models.application import Application
from base.views import BaseList, BaseExportView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


# Application

class ApplicationMixin:
    fields = ['name', 'status', 'description', 'univers', 'partner', 'comment']


class ApplicationList(BaseList):
    class ApplicationFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = Application
            fields = ['univers', 'partner']

    class ApplicationTable(BaseList.BaseTable):
        class Meta(BaseList.BaseTable.Meta):
            model = Application

    table_class = ApplicationTable
    model = Application
    filterset_class = ApplicationFilter

class ApplicationExportView(BaseExportView):
    template_name = "base/export.html"
    model = Application

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
