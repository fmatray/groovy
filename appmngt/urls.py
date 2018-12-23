# coding: utf8
"""
URLS
"""
from django.urls import path

from .views.application import ApplicationList, ApplicationDetailView, \
    ApplicationCreateView, ApplicationUpdateView, ApplicationDeleteView

urlpatterns = [
    path('application_list', ApplicationList.as_view()),
    path('application_detail/<int:pk>', ApplicationDetailView.as_view()),
    path('application_create',          ApplicationCreateView.as_view()),
    path('application_update/<int:pk>', ApplicationUpdateView.as_view()),
    path('application_delete/<int:pk>', ApplicationDeleteView.as_view())
]

