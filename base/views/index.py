from datetime import datetime
from itertools import chain
from operator import attrgetter

from appmngt.models.application import Application
from appmngt.models.environment import Environment
from appmngt.models.partner import Partner
from appmngt.models.release import Release
from appmngt.models.univers import Univers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from funcmngt.models.funcflow import FuncFlow
from funcmngt.models.subfuncflow import SubFuncFlow
from techmngt.models.asynchronous import AsynchronousFlow
from techmngt.models.batch import BatchFlow
from techmngt.models.network import NetworkFlow
from techmngt.models.server import Server
from techmngt.models.uri import URIFlow


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_releases'] = Release.objects.filter(release_date__gte=datetime.now()).all()
        context['univers'] = Univers.objects.all()
        context['partners'] = Partner.objects.all()
        models = [Application, Environment, Partner, Release, Univers,
                  FuncFlow, SubFuncFlow,
                  AsynchronousFlow, BatchFlow,NetworkFlow, URIFlow, Server]

        last_changes = [m.history.all()[:10] for m in models]
        last_changes = sorted(list(chain(*last_changes)), key=attrgetter('history_date'), reverse=True)[:10]
        context['last_changes'] = last_changes
        return context
