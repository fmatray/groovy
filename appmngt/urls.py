# coding: utf8
"""
URLS
"""
from django.urls import path

from .views.application import ApplicationList, ApplicationDetailView, \
    ApplicationCreateView, ApplicationUpdateView, ApplicationDeleteView
from .views.univers import UniversList, UniversDetailView, \
    UniversCreateView, UniversUpdateView, UniversDeleteView

urlpatterns = [
    path('application_list',            ApplicationList.as_view(),          name='application_list'),
    path('application_detail/<int:pk>', ApplicationDetailView.as_view(),    name='application_detail'),
    path('application_create',          ApplicationCreateView.as_view(),    name='application_create'),
    path('application_update/<int:pk>', ApplicationUpdateView.as_view(),    name='application_update'),
    path('application_delete/<int:pk>', ApplicationDeleteView.as_view(),    name='application_delete'),

    path('univers_list',                UniversList.as_view(),          name='univers_list'),
    path('univers_detail/<int:pk>',     UniversDetailView.as_view(),    name='univers_detail'),
    path('univers_create',              UniversCreateView.as_view(),    name='univers_create'),
    path('univers_update/<int:pk>',     UniversUpdateView.as_view(),    name='univers_update'),
    path('univers_delete/<int:pk>',     UniversDeleteView.as_view(),    name='univers_delete'),
]

