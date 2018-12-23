import django_filters
import django_tables2 as tables
from crispy_forms.layout import Submit
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.filters import CharFilter, ChoiceFilter
from django_filters.views import FilterView
from django_tables2 import SingleTableView

from base.forms import get_helper, get_inline_helper
from base.models import Base


class BaseMixin:
    fields = ['name', 'status', "description", 'comment']

class BaseList(FilterView, SingleTableView):
    class BaseFilter(django_filters.FilterSet):
        name = CharFilter(initial='')
        status = ChoiceFilter(choices=Base.STATUS)

        def __init__(self, *args, **kwargs):
            super(django_filters.FilterSet, self).__init__(*args, **kwargs)

            helper = get_inline_helper()
            helper.form_method = 'get'
            helper.form_action = ''
            helper.add_input(Submit('submit', 'Filter', css_class='btn-sm'))
            self.helper = helper

    class BaseTable(tables.Table):
        class Meta:
            template_name = "django_tables2/bootstrap4.html"

    template_name = "base/list.html"

    filterset_class = BaseFilter


class BaseDetailView(BaseMixin, DetailView):
    pass

class BaseCreateView(BaseMixin, CreateView):
    template_name = "base/form.html"

    def __init__(self, *args, **kwargs):
        super(CreateView, self).__init__(*args, **kwargs)
        self.helper = get_helper()


class BaseUpdateView(BaseMixin, UpdateView):
    template_name = "base/form.html"

    def __init__(self, *args, **kwargs):
        self.helper = get_helper()
        super(UpdateView, self).__init__(*args, **kwargs)


class BaseDeleteView(BaseMixin, DeleteView):
    template_name = "base/confirm_delete.html"
