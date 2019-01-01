from appmngt.models.release import Release
from base.forms import BaseForm


class ReleaseForm(BaseForm):
    class Meta (BaseForm.Meta):
        model = Release
