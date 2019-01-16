# coding: utf-8

"""
Module Base
"""
from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils.html import mark_safe
from markdown import markdown
from markdownx.models import MarkdownxField
from model_utils import Choices
from simple_history.models import HistoricalRecords
from taggit.managers import TaggableManager

from base.helpers import get_status_color
from django_cryptography.fields import encrypt

class Base(models.Model):
    STATUS = Choices('Draft', 'On going', 'Released', 'Retired', 'Abort')
    LIMIT_STATUS = {'status__in': ('On going', 'Released')}

    name = models.CharField("Name", max_length=200, blank=False, unique=True)
    status = models.CharField(choices=STATUS, default=STATUS.Draft, max_length=20)
    tags = TaggableManager(blank=True)
    description = encrypt(MarkdownxField("Description", null=True, blank=False,
                                 help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>"))
    documentation = encrypt(models.URLField("Documentation", null=True, blank=True))
    comment = encrypt(MarkdownxField("Comment", blank=True,
                             help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>"))

    history = HistoricalRecords(inherit=True)
    identification_fields = []
    identification_list_fields = []

    def get_status_badge(self):
        return "<span class='badge {}'>{}</span>".format(get_status_color(self.status), self.status)

    def get_description_as_markdown(self):
        return mark_safe(markdown(self.description, safe_mode='escape'))

    def get_comment_as_markdown(self):
        return mark_safe(markdown(self.comment, safe_mode='escape'))

    # URLS
    def get_list_url(self):
        try:
            return reverse('{}_list'.format(self._meta.model_name))
        except NoReverseMatch:
            return None

    def get_absolute_url(self):
        try:
            return reverse('{}_detail'.format(self._meta.model_name), args=(self.id,))
        except NoReverseMatch:
            return None

    def get_create_url(self, params=None):
        try:
            if params:
                return reverse('{}_create'.format(self._meta.model_name), args=(self.id,)) + "?{}".format(params)
            return reverse('{}_create'.format(self._meta.model_name))
        except NoReverseMatch:
            return None

    def get_update_url(self, params=None):
        try:
            if params:
                return reverse('{}_update'.format(self._meta.model_name), args=(self.id,)) + "?{}".format(params)
            return reverse('{}_update'.format(self._meta.model_name), args=(self.id,))
        except NoReverseMatch:
            return None

    def get_delete_url(self):
        try:
            return reverse('{}_delete'.format(self._meta.model_name), args=(self.id,))
        except NoReverseMatch:
            return None

    # Permissions
    @classmethod
    def get_perm(cls, perm):
        app, mdl = cls._meta.label_lower.split('.')
        return "{}.{}_{}".format(app, perm, mdl)

    @classmethod
    def get_view_perm(cls):
        return cls.get_perm('view')

    @classmethod
    def get_create_perm(cls):
        return cls.get_perm('add')

    @classmethod
    def get_update_perm(cls):
        return cls.get_perm('change')

    @classmethod
    def get_delete_perm(cls):
        return cls.get_perm('delete')

    def __str__(self):
        return self.name

    def meta(self):
        return self._meta

    class Meta:
        abstract = True
        ordering = ["name"]


class QuickLink(models.Model):
    name = models.CharField("Name", max_length=200, blank=False, unique=True)
    url = encrypt(models.URLField("URL", null=False, blank=False))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class BaseConfig(models.Model):
    name = models.CharField("Name", max_length=200, blank=False, unique=True)
    description = encrypt(MarkdownxField("Description", null=True, blank=False,
                                 help_text="<a href='https://en.wikipedia.org/wiki/Markdown'>You can use Markdown</a>"))
    history = HistoricalRecords(inherit=True)

    def __str__(self):
        return self.name

    def meta(self):
        return self._meta

    class Meta:
        abstract = True
        ordering = ["name"]