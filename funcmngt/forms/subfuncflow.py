from django_select2.forms import ModelSelect2Widget

from appmngt.models.application import Application
from base.forms import BaseForm
from funcmngt.models.funcflow import FuncFlow
from funcmngt.models.subfuncflow import SubFuncFlow


class SubFuncFlowForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = SubFuncFlow
        widgets = {
            'func_flow': ModelSelect2Widget(queryset=FuncFlow.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ]),
            'requester': ModelSelect2Widget(queryset=Application.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ]),
            'receiver': ModelSelect2Widget(queryset=Application.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ]),
        }
