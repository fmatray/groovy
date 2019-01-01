from appmngt.models.univers import Univers
from base.forms import BaseForm


class UniversForm(BaseForm):
    class Meta (BaseForm.Meta):
        model = Univers
