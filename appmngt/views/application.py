# coding: utf-8
"""
Application views
"""
from appmngt.models.application import Application
from base.views import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


class ApplicationMixin:
    fields = ['name', 'status', 'description', 'univers', 'partner', 'comment']


class ApplicationList(BaseList):
    class ApplicationFilter(BaseList.BaseFilter):
        class Meta:
            model = Application
            fields = ['univers', 'partner']

    class ApplicationTable(BaseList.BaseTable):
        class Meta(BaseList.BaseTable.Meta):
            model = Application

    table_class = ApplicationTable
    model = Application
    filterset_class = ApplicationFilter


class ApplicationDetailView(ApplicationMixin, BaseDetailView):
    model = Application


class ApplicationCreateView(ApplicationMixin, BaseCreateView):
    model = Application


class ApplicationUpdateView(ApplicationMixin, BaseUpdateView):
    model = Application


class ApplicationDeleteView(ApplicationMixin, BaseDeleteView):
    model = Application
