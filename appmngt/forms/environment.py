from appmngt.models.environment import Environment
from base.forms import BaseModalForm


class EnvironmentModalForm(BaseModalForm):
    class Meta(BaseModalForm.Meta):
        model = Environment
