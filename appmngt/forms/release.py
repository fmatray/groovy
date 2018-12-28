from appmngt.models.release import Release
from base.forms import BaseModalForm


class ReleaseModalForm(BaseModalForm):
    class Meta (BaseModalForm.Meta):
        model = Release
        fields = ['name', 'status', 'description', 'release_date',  'applications', 'comment']
