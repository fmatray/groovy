# coding: utf-8
"""
Univers views
"""
from django.urls import reverse_lazy

from appmngt.forms.univers import UniversModalForm
from appmngt.models.univers import Univers
from base.views import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


# Univers

class UniversMixin:
    pass

class UniversList(BaseList):
    class UniversFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = Univers

    class UniversTable(BaseList.BaseTable):
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
    form_class = UniversModalForm

# Update
class UniversUpdateView(BaseUpdateView):
    model = Univers
    success_message = 'Success: Univers was updated.'


# Delete
class UniversDeleteView(BaseDeleteView):
    model = Univers
    success_message = 'Success: Univers was deleted.'
    success_url = reverse_lazy('univers_list')
