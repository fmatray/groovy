# coding: utf-8
"""
Univers views
"""
from django.urls import reverse_lazy

from appmngt.models.univers import Univers
from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, BadgesColumn


# Univers
class UniversList(BaseList):
    class UniversFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = Univers

    class UniversTable(BaseList.BaseTable):
        app_univers = BadgesColumn(verbose_name="Applications", linkify_item=True)
        view_perms = {
            'app_univers': 'appmngt.view_application',
        }

        class Meta(BaseList.BaseTable.Meta):
            model = Univers

    table_class = UniversTable
    model = Univers
    filterset_class = UniversFilter


# Detail
class UniversDetailView(BaseDetailView):
    model = Univers


# Create
class UniversCreateView(BaseCreateView):
    model = Univers
    success_message = 'Success: Univers was created.'


# Update
class UniversUpdateView(BaseUpdateView):
    model = Univers
    success_message = 'Success: Univers was updated.'


# Delete
class UniversDeleteView(BaseDeleteView):
    model = Univers
    success_message = 'Success: Univers was deleted.'
    success_url = reverse_lazy('univers_list')
