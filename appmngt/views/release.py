# coding: utf-8
"""
Release views
"""

import django_tables2 as tables
from django.urls import reverse_lazy

from appmngt.models.release import Release
from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, BadgesColumn


# Release
class ReleaseList(BaseList):
    class ReleaseFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = Release
            exclude = ['id', 'tags', 'description', 'comment', 'applications', 'release_date']

    class ReleaseTable(BaseList.BaseTable):
        release_date = tables.DateColumn(format="D d/m/Y")
        applications = BadgesColumn(linkify_item=True)
        view_perms = {
            'applications': 'appmngt.view_application',
        }

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


# Update
class ReleaseUpdateView(BaseUpdateView):
    model = Release
    success_message = 'Success: Release was updated.'


# Delete
class ReleaseDeleteView(BaseDeleteView):
    model = Release
    success_message = 'Success: Release was deleted.'
    success_url = reverse_lazy('release_list')
