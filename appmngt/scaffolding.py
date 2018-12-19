# coding: utf-8
"""
CRUD
"""
from django.contrib.auth.decorators import login_required
from base.scaffolding import BaseCrudManager

from .models.application import Application
from .models.environment import Environment
from .models.partner import Partner
from .models.release import Release
from .models.univers import Univers


class ApplicationCrudManager(BaseCrudManager):
    model = Application
    prefix = 'application_'

class EnvironmentCrudManager(BaseCrudManager):
    model = Environment
    prefix = 'environment_'

class PartnerCrudManager(BaseCrudManager):
    model = Partner
    prefix = 'partner_'

class ReleaseCrudManager(BaseCrudManager):
    model = Release
    prefix = 'release_'

