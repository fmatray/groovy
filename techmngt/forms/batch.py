from django_select2.forms import ModelSelect2Widget

from base.forms import BaseForm
from funcmngt.models.subfuncflow import SubFuncFlow
from techmngt.models.asynchronous import AsynchronousFlow
from techmngt.models.batch import BatchFlow


class BatchFlowForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = BatchFlow
        widgets = {
            'subfunc_flow': ModelSelect2Widget(queryset=SubFuncFlow.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ]),

            'input_flow': ModelSelect2Widget(queryset=AsynchronousFlow.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ]),
            'output_flow': ModelSelect2Widget(queryset=AsynchronousFlow.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ])
        }
