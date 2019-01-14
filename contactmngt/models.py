from appmngt.models.partner import Partner
from base.models import Base
from django.db import models
from django.urls import reverse, NoReverseMatch
from django_cryptography.fields import encrypt
from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords


class Contact(models.Model):
    """Contact model."""

    phone_number = encrypt(PhoneNumberField('Phone number', blank=True))
    email_address = encrypt(models.EmailField('email address', blank=True))

    web_site = encrypt(models.URLField('Web site', blank=True))

    street = encrypt(models.TextField('street', blank=True))
    city = encrypt(models.CharField('city', max_length=200, blank=True))
    province = encrypt(models.CharField('province', max_length=200, blank=True))
    postal_code = encrypt(models.CharField('postal code', max_length=10, blank=True))
    country = encrypt(models.CharField('country', max_length=100, blank=True))

    about = encrypt(models.TextField('about', blank=True))
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
    def meta(self):
        return self._meta
    class Meta:
        abstract = True


class Team(Contact):
    icon = "fas fa-users"
    name = encrypt(models.CharField('Name', max_length=100))
    departement = encrypt(models.CharField('Department', max_length=100))
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT, verbose_name="Partner",
                                limit_choices_to=Base.LIMIT_STATUS,
                                default=None, blank=False, null=False, related_name="team_partner")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        unique_together = ('name', 'departement', 'partner')

class Person(Contact):
    icon = "fas fa-user"
    first_name = encrypt(models.CharField('first name', max_length=100))
    last_name = encrypt(models.CharField('last name', max_length=200))
    title = encrypt(models.CharField('title', max_length=200, blank=True))
    team = models.ForeignKey(Team, on_delete=models.PROTECT, verbose_name="Team",
                             default=None, blank=False, null=False, related_name="person_team")

    def name(self):
        return self.__str__()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
