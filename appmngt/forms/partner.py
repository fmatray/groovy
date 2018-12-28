from appmngt.models.partner import Partner
from base.forms import BaseModalForm


class PartnerModalForm(BaseModalForm):
    class Meta(BaseModalForm.Meta):
        model = Partner
