from base.forms import BaseForm
from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget
from funcmngt.models.subfuncflow import SubFuncFlow
from techmngt.models.server import Server
from techmngt.models.synchronous import SynchronousFlow


class SynchronousFlowForm(BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            app_list = []
            try:
                app_list.append(self.instance.subfunc_flow.receiver)
            except:
                pass
            try:
                app_list.append(self.instance.subfunc_flow.requester)
            except:
                pass
            if app_list:
                self.fields['servers'].widget.queryset = Server.objects.filter(status__in=('On going', 'Released'),
                                                                               env_servers__application__in=app_list)

    class Meta(BaseForm.Meta):
        model = SynchronousFlow
        widgets = {
            'subfunc_flow': ModelSelect2Widget(queryset=SubFuncFlow.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ]),
            'servers': ModelSelect2MultipleWidget(queryset=Server.objects.none(), search_fields=['name__icontains', ])
        }
