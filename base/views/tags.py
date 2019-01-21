import django_filters
import django_tables2 as tables
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.detail import DetailView
from django_filters.filters import CharFilter
from django_filters.filters import CharFilter, ChoiceFilter
from django_filters.views import FilterView
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from taggit.models import Tag, TaggedItem

from .modelviews import BadgesColumn

TaggedItem.get_absolute_url = lambda obj: obj.content_object.get_absolute_url()
TaggedItem.__str__ = lambda obj: obj.content_object.__str__()
Tag.get_absolute_url = lambda obj: reverse('tag', args=(obj.slug,))


class TagListView(FilterView, SingleTableView):
    strict = False

    class TagFilter(django_filters.FilterSet):
        name = CharFilter(lookup_expr='contains')

        class Meta:
            model = Tag
            fields = ['name']

    class TagTable(tables.Table):
        name = tables.Column(linkify=("tag", (tables.A("slug"),)))
        taggit_taggeditem_items = BadgesColumn(verbose_name='Tagged objects', linkify_item=True)

        class Meta:
            model = Tag
            fields = ['name']
            template_name = "layout/table.html"

    template_name = "base/tags.html"
    filterset_class = TagFilter
    table_class = TagTable
    model = Tag


class TagView(LoginRequiredMixin, DetailView):
    template_name = "base/tag.html"
    model = Tag
