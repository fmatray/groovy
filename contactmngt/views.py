import django_filters
import django_tables2 as tables
from contactmngt.models import Team, Person
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.html import conditional_escape
from django.views import generic
from django.views.generic.detail import DetailView
from django_filters.filters import CharFilter, ChoiceFilter
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from django_tables2.export.views import ExportMixin
from contactmngt.forms import TeamForm

class TeamMixin(LoginRequiredMixin):
    perm = ''


class TeamList(TeamMixin, FilterView, ExportMixin, SingleTableView):
    perm = 'view'
    # all data if no filter
    strict = False

    class TeamFilter(django_filters.FilterSet):
        class Meta:
            model = Team
            fields = ['name', 'partner']

    class TeamTable(tables.Table):
        view_perms = {}

        class Meta:
            model = Team
            template_name = "layout/table.html"
            exclude = ['id']
            sequence = ['name', 'departement', 'partner', '...']

    table_class = TeamTable
    filterset_class = TeamFilter
    template_name = "contactmngt/contact_list.html"
    model = Team


class TeamDetailView(TeamMixin, DetailView):
    perm = 'view'
    model = Team



class TeamCreateUpdateMixin(TeamMixin):
    model = Team
    template_name = 'contactmngt/team_form.html'
    form_class = TeamForm

    def get_initial(self):
        if self.request.GET:
            return self.request.GET.dict()
        return super().get_initial()


class TeamCreateView(TeamCreateUpdateMixin, SuccessMessageMixin, generic.CreateView):
    perm = 'add'


class TeamUpdateView(TeamCreateUpdateMixin, SuccessMessageMixin, generic.UpdateView):
    perm = 'change'


class TeamDeleteView(TeamMixin, generic.DeleteView):
    perm = 'delete'
    template_name = "base/confirm_delete.html"
