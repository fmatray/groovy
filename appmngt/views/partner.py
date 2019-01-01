# coding: utf-8
"""
Partner views
"""
from django.urls import reverse_lazy

from appmngt.forms.partner import PartnerForm
from appmngt.models.partner import Partner
from base.views.modelviews import BaseList, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView, BadgesColumn


# Partner

class PartnerMixin:
    pass


class PartnerList(BaseList):
    class PartnerFilter(BaseList.BaseFilter):
        class Meta(BaseList.BaseFilter.Meta):
            model = Partner

    class PartnerTable(BaseList.BaseTable):
        app_partner = BadgesColumn(verbose_name="Applications", linkify_item=True)
        view_perms = {
            'app_partner': 'appmngt.view_application',
        }

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
    form_class = PartnerForm


# Update
class PartnerUpdateView(BaseUpdateView):
    model = Partner
    success_message = 'Success: Partner was updated.'
    form_class = PartnerForm


# Delete
class PartnerDeleteView(BaseDeleteView):
    model = Partner
    success_message = 'Success: Partner was deleted.'
    success_url = reverse_lazy('partner_list')
