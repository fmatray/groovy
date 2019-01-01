from appmngt.models.application import Application
from base.forms import BaseForm



class ApplicationForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = Application
