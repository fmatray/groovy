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
from contactmngt.forms import TeamForm, PersonForm

class TeamMixin(LoginRequiredMixin):
    perm = ''


class TeamList(TeamMixin, FilterView, ExportMixin, SingleTableView):
    perm = 'view'
    # all data if no filter
    strict = False

    class TeamFilter(django_filters.FilterSet):
        name = CharFilter(lookup_expr='contains')
        class Meta:
            model = Team
            fields = ['name', 'partner']

    class TeamTable(tables.Table):
        name = tables.LinkColumn()
        partner = tables.LinkColumn()
        view_perms = {}

        class Meta:
            model = Team
            template_name = "layout/table.html"
            exclude = ['id', 'about']
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
    model = Team
    template_name = "base/confirm_delete.html"


"""--------------- PERSONS ---------------"""

class PersonMixin(LoginRequiredMixin):
    perm = ''


class PersonList(PersonMixin, FilterView, ExportMixin, SingleTableView):
    perm = 'view'
    # all data if no filter
    strict = False

    class PersonFilter(django_filters.FilterSet):
        class Meta:
            model = Person
            fields = ['team']

    class PersonTable(tables.Table):
        first_name = tables.LinkColumn()
        last_name = tables.LinkColumn()
        team = tables.LinkColumn()

        view_perms = {}

        class Meta:
            model = Person
            template_name = "layout/table.html"
            exclude = ['id', 'about']
            sequence = ['first_name', 'last_name', 'title', 'team', '...']

    table_class = PersonTable
    filterset_class = PersonFilter
    template_name = "contactmngt/contact_list.html"
    model = Person


class PersonDetailView(PersonMixin, DetailView):
    perm = 'view'
    model = Person



class PersonCreateUpdateMixin(PersonMixin):
    model = Person
    template_name = 'contactmngt/person_form.html'
    form_class = PersonForm

    def get_initial(self):
        if self.request.GET:
            return self.request.GET.dict()
        return super().get_initial()


class PersonCreateView(PersonCreateUpdateMixin, SuccessMessageMixin, generic.CreateView):
    perm = 'add'


class PersonUpdateView(PersonCreateUpdateMixin, SuccessMessageMixin, generic.UpdateView):
    perm = 'change'


class PersonDeleteView(PersonMixin, generic.DeleteView):
    perm = 'delete'
    model = Person
    template_name = "base/confirm_delete.html"

