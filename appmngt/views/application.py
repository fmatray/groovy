import django_filters
from crispy_forms.helper import FormHelper
from django_filters.views import FilterView
from django_tables2 import SingleTableView

from appmngt.models.application import Application
from appmngt.tables.application import ApplicationTable


class ApplicationFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(django_filters.FilterSet, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form form-inline'
        self.helper.form_method = 'get'
        self.helper.form_action = ''
        self.helper.label_class = 'col'
        self.helper.field_class = 'col'
        self.helper.field_classes = 'form-control-sm'
        self.helper.template= 'groovy/whole_uni_form.html'

    class Meta:
        model = Application
        fields = ['name', 'univers', 'partner']


class ApplicationList(FilterView, SingleTableView):
    table_class = ApplicationTable
    model = Application

    template_name = "base/list.html"

    filterset_class = ApplicationFilter
