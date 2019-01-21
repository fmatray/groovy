import django_filters
import django_tables2 as tables
from base.helpers import get_status_color
from base.models import Base
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.utils.html import conditional_escape
from django.views import generic
from django.views.generic.detail import DetailView
from django_filters.filters import CharFilter, ChoiceFilter
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from django_tables2.export.views import ExportMixin
from django.contrib import messages

class BaseMixin(LoginRequiredMixin, PermissionRequiredMixin, AccessMixin):
    perm = ''

    def get_permission_required(self):
        app, mdl = self.model._meta.label_lower.split('.')
        return ("{}.{}_{}".format(app, self.perm, mdl),)


class SingleBadgeColumn(tables.Column):
    def render(self, value):
        if not value:
            return "—"

        content = "<span class='badge badge-primary'>{}</span>".format(value)
        if hasattr(value, "get_absolute_url"):
            link = value.get_absolute_url()
        else:
            link = self.link
        if link:
            content = "<a href='{}'>{}</a>".format(value.get_absolute_url(), content)
        return content

    def value(self, **kwargs):
        return kwargs['value']


class StatusColumn(tables.Column):
    def render(self, value):
        return "<span class='badge {}'>{}</span>".format(get_status_color(value), value)

    def value(self, **kwargs):
        return kwargs['value']



class BadgesColumn(tables.ManyToManyColumn):
    def render(self, value):
        # if value is None or not value.exists():
        if not value.exists():
            return "—"
        tags = ""
        for item in self.filter(value):
            content = conditional_escape(self.transform(item))
            content = "<span class='badge badge-pill badge-primary mx-1'>{}</span>".format(content)
            if hasattr(item, "get_absolute_url"):
                content = "<a href='{}'>{}</a>".format(item.get_absolute_url(), content)
            tags += content
        return tags

    def value(self, **kwargs):
        return ", ".join([i.name for i in kwargs['value'].all()])


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
            exclude = ['id', 'tags', 'description', 'pin', 'documentation', 'comment']

    class BaseTable(tables.Table):
        name = tables.LinkColumn()
        status = StatusColumn()
        tags = BadgesColumn()
        fields = ['name', 'status', 'tags']
        view_perms = {}

        def before_render(self, request):
            """implement permissions"""
            for col, perm in self.view_perms.items():
                if not request.user.has_perm(perm):
                    self.columns.hide(col)

        class Meta:
            template_name = "layout/table.html"
            exclude = ['id', 'description', 'pin', 'documentation', 'comment']

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


class BaseDeleteView(BaseMixin, SuccessMessageMixin, generic.DeleteView):
    perm = 'delete'
    template_name = "base/confirm_delete.html"

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            obj = self.get_object()
            error_url = obj.get_absolute_url()
            messages.error(self.request, 'Object cannot be delete as it is related to another one.')
            return HttpResponseRedirect(error_url)
