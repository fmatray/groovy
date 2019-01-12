from django_select2.forms import ModelSelect2Widget

from appmngt.models.application import Application
from appmngt.models.partner import Partner
from appmngt.models.univers import Univers
from base.forms import BaseForm


class ApplicationForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = Application
        widgets = {
            'univers': ModelSelect2Widget(queryset=Univers.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ]),
            'partner': ModelSelect2Widget(queryset=Partner.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields = ['name__icontains',])
        }
