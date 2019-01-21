from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from taggit.models import Tag, TaggedItem

class TagView(LoginRequiredMixin, DetailView):
    template_name = "base/tag.html"
    model = Tag