from appmngt.models.partner import Partner
from base.models import Base
from django.db import models

from django.urls import reverse, NoReverseMatch
from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords


class Contact(models.Model):
    """Contact model."""

    phone_number = PhoneNumberField('Phone number', blank=True)
    email_address = models.EmailField('email address', blank=True)

    web_site = models.URLField('Web site', blank=True)

    street = models.TextField('street', blank=True)
    city = models.CharField('city', max_length=200, blank=True)
    province = models.CharField('province', max_length=200, blank=True)
    postal_code = models.CharField('postal code', max_length=10, blank=True)
    country = models.CharField('country', max_length=100, blank=True)

    about = models.TextField('about', blank=True)
    history = HistoricalRecords(inherit=True)

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

    class Meta:
        abstract = True


class Team(Contact):
    name = models.CharField('Name', max_length=100)
    departement = models.CharField('Department', max_length=100)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name="Partner",
                                limit_choices_to=Base.LIMIT_STATUS,
                                default=None, blank=True, null=True, related_name="team_partner")

    def __str__(self):
        return self.name


class Person(Contact):
    first_name = models.CharField('first name', max_length=100)
    last_name = models.CharField('last name', max_length=200)
    title = models.CharField('title', max_length=200, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Team",
                             default=None, blank=False, null=False, related_name="person_team")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
