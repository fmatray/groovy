# coding: utf-8
"""
Partner views
"""
import django_tables2 as tables
from django.urls import reverse_lazy

from appmngt.forms.partner import PartnerModalForm
from appmngt.models.partner import Partner
from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


# Partner

class PartnerMixin:
    pass


class PartnerList(BaseList):
    class PartnerFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = Partner

    class PartnerTable(BaseList.BaseTable):
        app_partner = tables.ManyToManyColumn(verbose_name="Applications", linkify_item=True)

        class Meta(BaseList.BaseTable.Meta):
            model = Partner

    table_class = PartnerTable
    model = Partner
    filterset_class = PartnerFilter


# Detail
class PartnerDetailView(BaseDetailView):
    model = Partner


# Create
class PartnerCreateView(BaseCreateView):
    model = Partner
    success_message = 'Success: Partner was created.'
    form_class = PartnerModalForm


# Update
class PartnerUpdateView(BaseUpdateView):
    model = Partner
    success_message = 'Success: Partner was updated.'
    form_class = PartnerModalForm


# Delete
class PartnerDeleteView(BaseDeleteView):
    model = Partner
    success_message = 'Success: Partner was deleted.'
    success_url = reverse_lazy('partner_list')
