from django_select2.forms import ModelSelect2Widget

from base.forms import BaseForm
from funcmngt.models.subfuncflow import SubFuncFlow
from techmngt.models.uri import URIFlow


class URIFlowForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = URIFlow
        widgets = {
            'subfunc_flow': ModelSelect2Widget(queryset=SubFuncFlow.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ]),
        }
