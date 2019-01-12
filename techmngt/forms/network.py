from django_select2.forms import ModelSelect2Widget

from base.forms import BaseForm
from techmngt.models.network import NetworkFlow
from techmngt.models.server import Server


class NetworkFlowForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = NetworkFlow
        widgets = {
            'source_server': ModelSelect2Widget(queryset=Server.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ]),
            'destination_server': ModelSelect2Widget(queryset=Server.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ])
        }
