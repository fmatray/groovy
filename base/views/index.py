from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from appmngt.models.release import Release
from appmngt.models.univers import Univers
from appmngt.models.partner import Partner

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_releases'] = Release.objects.filter(release_date__gte=datetime.now()).all()
        context['univers'] = Univers.objects.all()
        context['partners'] = Partner.objects.all()
        return context
