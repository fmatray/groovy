from base.forms import BaseForm
from techmngt.models.server import Server


class ServerForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = Server
