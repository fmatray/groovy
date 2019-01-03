# coding: utf-8

"""
Module Base
"""
from base.helpers import get_status_color
from django.db import models
from django.urls import reverse, NoReverseMatch
from model_utils import Choices
from simple_history.models import HistoricalRecords
from taggit.managers import TaggableManager


class Base(models.Model):
    STATUS = Choices('Draft', 'On going', 'Released', 'Retired', 'Abort')
    LIMIT_STATUS = {'status__in':('On going', 'Released')}

    name = models.CharField("Name", max_length=200, blank=False, unique=True)
    status = models.CharField(choices=STATUS, default=STATUS.Draft, max_length=20)
    tags = TaggableManager(blank=True)
    description = models.TextField("Description", null=True, blank=True)
    comment = models.TextField("Comment", blank=True)

    history = HistoricalRecords(inherit=True)
    identification_fields = []
    identification_list_fields = []

    def get_status_badge(self):
        return "<span class='badge badge-pill {}'>{}</span>".format(get_status_color(self.status), self.status)

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
