from base.forms import BaseForm
from funcmngt.models.funcflow import FuncFlow


class FuncFlowForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = FuncFlow
