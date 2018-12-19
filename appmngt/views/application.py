import django_filters
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from appmngt.models.application import Application
from appmngt.tables.application import ApplicationTable


class ApplicationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Application
        fields = ['name']

class ApplicationList(SingleTableView, FilterView):
    model = Application
    table_class = ApplicationTable
    filterset_class = ApplicationFilter

    template_name = "base/list.html"
