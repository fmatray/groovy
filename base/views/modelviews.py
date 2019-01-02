import django_filters
import django_tables2 as tables
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.html import conditional_escape
from django.views import generic
from django.views.generic.detail import DetailView
from django_filters.filters import CharFilter, ChoiceFilter
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from django_tables2.export.views import ExportMixin
from django_tables2.utils import A

from base.helpers import get_status_color
from base.models import Base


class BaseMixin(LoginRequiredMixin, PermissionRequiredMixin, AccessMixin):
    perm = ''

    def get_permission_required(self):
        app, mdl = self.model._meta.label_lower.split('.')
        return ("{}.{}_{}".format(app, self.perm, mdl),)


class SingleBadgeColumn(tables.Column):
    def render(self, value):
        content = "<span class='badge badge-pill badge-primary'>{}</span>".format(value)
        if hasattr(value, "get_absolute_url"):
            content = "<a href='{}'>{}</a>".format(value.get_absolute_url(), content)
        return content


class StatusColumn(tables.Column):
    def render(self, value):
        return "<span class='badge badge-pill {}'>{}</span>".format(get_status_color(value), value)
        return value


class BadgesColumn(tables.ManyToManyColumn):
    def render(self, value):
        # if value is None or not value.exists():
        if not value.exists():
            return "-"

        tags = ""
        for item in self.filter(value):
            content = conditional_escape(self.transform(item))
            content = "<span class='badge badge-pill badge-primary'>{}</span>".format(content)
            if hasattr(item, "get_absolute_url"):
                content = "<a href='{}'>{}</a>".format(item.get_absolute_url(), content)
            tags += content
        return tags


class BaseList(BaseMixin, FilterView, ExportMixin, SingleTableView):
    perm = 'view'
    # all data if no filter
    strict = False

    def get_filterset(self, filterset_class):
        """get filterset with permissions"""
        _filterset_class = super().get_filterset(filterset_class)

        for f in list(_filterset_class.filters.keys()):
            try:
                if not self.request.user.has_perm(_filterset_class.filters[f].field._queryset.model.get_view_perm()):
                    print("deleting", f)
                    del _filterset_class.filters[f]
            except AttributeError:
                pass
        return _filterset_class

    class BaseFilter(django_filters.FilterSet):
        name = CharFilter(lookup_expr='contains')
        status = ChoiceFilter(choices=Base.STATUS)

        class Meta:
            exclude = ['id', 'tags', 'description', 'comment']

    class BaseTable(tables.Table):
        name = tables.LinkColumn(args=[A('pk')])
        status = StatusColumn()
        tags = BadgesColumn()
        fields = ['name', 'status', 'tags']
        export_formats = ['csv', 'xls', 'json']
        view_perms = {}

        def before_render(self, request):
            """implement permissions"""
            for col, perm in self.view_perms.items():
                if not request.user.has_perm(perm):
                    self.columns.hide(col)

        class Meta:
            template_name = "layout/table.html"
            exclude = ['id', 'description', 'comment']

    template_name = "base/list.html"
    filterset_class = BaseFilter


class BaseDetailView(BaseMixin, DetailView):
    perm = 'view'


class BaseCreateUpdateMixin(BaseMixin):
    def get_initial(self):
        if self.request.GET:
            return self.request.GET.dict()
        return super().get_initial()


class BaseCreateView(BaseCreateUpdateMixin, SuccessMessageMixin, generic.CreateView):
    perm = 'add'
    template_name = 'base/form.html'


class BaseUpdateView(BaseCreateUpdateMixin, SuccessMessageMixin, generic.UpdateView):
    perm = 'change'
    template_name = 'base/form.html'


class BaseDeleteView(BaseMixin, generic.DeleteView):
    perm = 'delete'
    template_name = "base/confirm_delete.html"