# coding: utf8
"""
URLS
"""
from django.conf import settings
from django.urls import path
from .views.application import ApplicationList
from .scaffolding import ApplicationCrudManager, EnvironmentCrudManager, PartnerCrudManager, ReleaseCrudManager


urlpatterns = [
 path('application_list', ApplicationList.as_view()),

]


"""crud_list = [ApplicationCrudManager, EnvironmentCrudManager, PartnerCrudManager, ReleaseCrudManager]
for crud in crud_list:
 urlpatterns += crud().get_url_patterns()
"""