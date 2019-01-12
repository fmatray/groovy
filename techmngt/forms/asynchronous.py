from base.forms import BaseForm
from techmngt.models.asynchronous import AsynchronousFlow


class AsynchronousFlowForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = AsynchronousFlow
