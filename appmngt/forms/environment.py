from django.core.exceptions import ObjectDoesNotExist

from appmngt.models.environment import Environment
from base.forms import BaseForm


class EnvironmentForm(BaseForm):

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data['name'].lower()
        app = cleaned_data['application']
        try:
            Environment.objects.get(name__iexact=name, application=app)
            self.add_error('name', 'Name and application must be unique together')
        except ObjectDoesNotExist:
            pass
        return cleaned_data

    class Meta(BaseForm.Meta):
        model = Environment
