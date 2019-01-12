from django_select2.forms import ModelSelect2MultipleWidget

from appmngt.models.application import Application
from appmngt.models.release import Release
from base.forms import BaseForm


class ReleaseForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = Release
        widgets = {
            'applications': ModelSelect2MultipleWidget(queryset=Application.objects.filter(
                status__in=('On going', 'Released')).all(), search_fields=['name__icontains', ])
        }
