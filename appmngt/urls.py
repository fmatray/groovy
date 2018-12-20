# coding: utf8
"""
URLS
"""
from django.conf import settings
from django.urls import path
from .views.application import ApplicationList


urlpatterns = [
 path('application_list', ApplicationList.as_view()),

]