from appmngt.models.univers import Univers
from base.forms import BaseModalForm


class UniversModalForm(BaseModalForm):
    class Meta (BaseModalForm.Meta):
        model = Univers
