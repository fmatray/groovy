from appmngt.models.application import Application
from base.forms import BaseModalForm


class ApplicationModalForm(BaseModalForm):
    class Meta (BaseModalForm.Meta):
        model = Application
