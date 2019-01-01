from appmngt.models.partner import Partner
from base.forms import BaseForm


class PartnerForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = Partner
