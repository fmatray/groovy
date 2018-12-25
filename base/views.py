import django_filters
import django_tables2 as tables
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.filters import CharFilter, ChoiceFilter
from django_filters.views import FilterView
from django_tables2 import SingleTableView

from base.models import Base


class BaseMixin(LoginRequiredMixin, PermissionRequiredMixin, AccessMixin):
    fields = ['name', 'status', "description", 'comment']
    perm = ''

    def get_permission_required(self):
        app, mdl = self.model._meta.label_lower.split('.')
        return "{}.{}_{}".format(app, self.perm, mdl)


class BaseList(BaseMixin, FilterView, SingleTableView):
    perm = 'view'

    class BaseFilter(django_filters.FilterSet):
        name = CharFilter(initial='')
        status = ChoiceFilter(choices=Base.STATUS)

    class BaseTable(tables.Table):
        class Meta:
            template_name = "django_tables2/bootstrap4.html"

    template_name = "base/list.html"

    filterset_class = BaseFilter


class BaseDetailView(BaseMixin, DetailView):
    perm = 'view'


class BaseCreateView(BaseMixin, CreateView):
    perm = 'add'
    template_name = "base/form.html"


class BaseUpdateView(BaseMixin, UpdateView):
    perm = 'change'
    template_name = "base/form.html"

class BaseDeleteView(BaseMixin, DeleteView):
    perm = 'delete'
    template_name = "base/confirm_delete.html"
