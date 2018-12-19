import django_tables2 as tables
from appmngt.models.application import Application

class ApplicationTable(tables.Table):
    class Meta:
        model = Application
        template_name = "django_tables2/bootstrap4.html"
        attrs = {'class': 'table'}
