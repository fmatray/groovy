# coding: utf-8

"""
Module Base
"""
from django.db import models
from django.urls import reverse, NoReverseMatch
from model_utils import Choices
from simple_history.models import HistoricalRecords
from taggit.managers import TaggableManager

class Base(models.Model):
    STATUS = Choices('Draft', 'On going', 'Released', 'Retired', 'Abort')

    name = models.CharField("Name", max_length=200, blank=False, unique=True)
    description = models.TextField("Description", null=True, blank=True)
    comment = models.TextField("Comment", blank=True)
    status = models.CharField(choices=STATUS, default=STATUS.Draft, max_length=20)

    tags = TaggableManager(blank=True)
    history = HistoricalRecords(inherit=True)


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
                return reverse('{}_update'.format(self._meta.model_name), args=(self.id,)) + "?{}".format(params)
            return reverse('{}_create'.format(self._meta.model_name))
        except NoReverseMatch:
            return None


    def get_update_url(self):
        try:
            return reverse('{}_update'.format(self._meta.model_name), args=(self.id,))
        except NoReverseMatch:
            return None

    def get_delete_url(self):
        try:
            return reverse('{}_delete'.format(self._meta.model_name), args=(self.id,))
        except NoReverseMatch:
            return None


    def __str__(self):
        return self.name

    def meta(self):
        return self._meta

    class Meta:
        abstract = True
        ordering = ["name"]
