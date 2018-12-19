# coding: utf-8

"""
Module Base
"""
from django.db import models
from simple_history.models import HistoricalRecords
from model_utils import Choices
from taggit.managers import TaggableManager

class Base(models.Model):
    STATUS = Choices('Draft', 'To do', 'Doing', 'Done', 'Abort', 'Retired')

    name = models.CharField("Nom", max_length=200, blank=False)
    description = models.TextField("Description", null=True, blank=True)
    comment = models.TextField("Comment", blank=True)
    status = models.CharField(choices=STATUS, default=STATUS.Draft, max_length=20)

    tags = TaggableManager(blank=True)
    history = HistoricalRecords(inherit=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ["name"]
