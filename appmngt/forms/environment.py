from django.core.exceptions import ObjectDoesNotExist
from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget

from appmngt.models.application import Application
from appmngt.models.environment import Environment
from base.forms import BaseForm
from techmngt.models.server import Server


class EnvironmentForm(BaseForm):

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data['name'].lower()
        app = cleaned_data['application']
        try:
            env = Environment.objects.get(name__iexact=name, application=app)
            if self.instance != env:
                self.add_error('name', 'Name and application must be unique together')
        except ObjectDoesNotExist:
            pass
        return cleaned_data

    class Meta(BaseForm.Meta):
        model = Environment
        widgets = {
            'application': ModelSelect2Widget(queryset=Application.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ]),
            'servers': ModelSelect2MultipleWidget(queryset=Server.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ])
        }
