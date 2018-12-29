import django_filters
import django_tables2 as tables
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.views.generic.detail import DetailView
from django_filters.filters import CharFilter, ChoiceFilter
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from django_tables2.export.views import ExportMixin
from django_tables2.utils import A

from base.models import Base


class BaseMixin(LoginRequiredMixin, PermissionRequiredMixin, AccessMixin):
    fields = ['name', 'status', "description", 'comment']
    perm = ''

    def get_permission_required(self):
        app, mdl = self.model._meta.label_lower.split('.')
        return "{}.{}_{}".format(app, self.perm, mdl)


class BaseList(BaseMixin, FilterView, ExportMixin, SingleTableView):
    perm = 'view'

    class BaseFilter(django_filters.FilterSet):
        name = CharFilter(initial='')
        status = ChoiceFilter(choices=Base.STATUS)

        class Meta:
            fields = []

    class BaseTable(tables.Table):
        name = tables.LinkColumn(args=[A('pk')])
        status = tables.Column()
        tags = tables.ManyToManyColumn()
        fields = ['name', 'status', 'tags']
        export_formats = ['csv', 'xls', 'json']

        class Meta:
            template_name = "layout/table.html"
            exclude = ['id', 'description', 'comment']

    template_name = "base/list.html"

    filterset_class = BaseFilter


class BaseDetailView(BaseMixin, DetailView):
    perm = 'view'


class BaseCreateUpdateMixin():
    def get_initial(self):
        if self.request.GET:
            return self.request.GET.dict()
        return super().get_initial()


class BaseCreateView(BaseCreateUpdateMixin, PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    perm = 'add'
    template_name = 'base/form_modal.html'


class BaseUpdateView(BaseCreateUpdateMixin, PassRequestMixin, SuccessMessageMixin, generic.UpdateView):
    perm = 'change'
    template_name = 'base/form_modal.html'


class BaseDeleteView(DeleteAjaxMixin, generic.DeleteView):
    perm = 'delete'
    template_name = "base/confirm_delete.html"
