# coding: utf-8
"""
Release views
"""

import django_tables2 as tables
from django.urls import reverse_lazy

from appmngt.forms.release import ReleaseModalForm
from appmngt.models.release import Release
from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


# Release

class ReleaseMixin:
    fields = ['name', 'status', 'description', 'comment']


class ReleaseList(BaseList):
    class ReleaseFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = Release

    class ReleaseTable(BaseList.BaseTable):
        release_date = tables.DateColumn(format="D d/m/Y")
        applications = tables.ManyToManyColumn(linkify_item=True)

        class Meta(BaseList.BaseTable.Meta):
            model = Release

    table_class = ReleaseTable
    model = Release
    filterset_class = ReleaseFilter


# Detail
class ReleaseDetailView(BaseDetailView):
    model = Release


# Create
class ReleaseCreateView(BaseCreateView):
    model = Release
    success_message = 'Success: Release was created.'
    form_class = ReleaseModalForm


# Update
class ReleaseUpdateView(BaseUpdateView):
    model = Release
    success_message = 'Success: Release was updated.'
    form_class = ReleaseModalForm


# Delete
class ReleaseDeleteView(BaseDeleteView):
    model = Release
    success_message = 'Success: Release was deleted.'
    success_url = reverse_lazy('release_list')
