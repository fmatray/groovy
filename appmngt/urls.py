# coding: utf8
"""
URLS
"""
from django.urls import path

from .views.application import ApplicationList, ApplicationDetailView, \
    ApplicationCreateView, ApplicationUpdateView, ApplicationDeleteView
from .views.environment import EnvironmentList, EnvironmentDetailView, \
    EnvironmentCreateView, EnvironmentUpdateView, EnvironmentDeleteView
from .views.partner import PartnerList, PartnerDetailView, \
    PartnerCreateView, PartnerUpdateView, PartnerDeleteView
from .views.release import ReleaseList, ReleaseDetailView, \
    ReleaseCreateView, ReleaseUpdateView, ReleaseDeleteView
from .views.univers import UniversList, UniversDetailView, \
    UniversCreateView, UniversUpdateView, UniversDeleteView

urlpatterns = [
    path('application_list',            ApplicationList.as_view(),          name='application_list'),
    path('application_detail/<int:pk>', ApplicationDetailView.as_view(),    name='application_detail'),
    path('application_create',          ApplicationCreateView.as_view(),    name='application_create'),
    path('application_update/<int:pk>', ApplicationUpdateView.as_view(),    name='application_update'),
    path('application_delete/<int:pk>', ApplicationDeleteView.as_view(),    name='application_delete'),

    path('environment_list',            EnvironmentList.as_view(),          name='environment_list'),
    path('environment_detail/<int:pk>', EnvironmentDetailView.as_view(),    name='environment_detail'),
    path('environment_create',          EnvironmentCreateView.as_view(),    name='environment_create'),
    path('environment_update/<int:pk>', EnvironmentUpdateView.as_view(),    name='environment_update'),
    path('environment_delete/<int:pk>', EnvironmentDeleteView.as_view(),    name='environment_delete'),

    path('partner_list',                PartnerList.as_view(),              name='partner_list'),
    path('partner_detail/<int:pk>',     PartnerDetailView.as_view(),        name='partner_detail'),
    path('partner_create',              PartnerCreateView.as_view(),        name='partner_create'),
    path('partner_update/<int:pk>',     PartnerUpdateView.as_view(),        name='partner_update'),
    path('partner_delete/<int:pk>',     PartnerDeleteView.as_view(),        name='partner_delete'),

    path('release_list',                ReleaseList.as_view(),              name='release_list'),
    path('release_detail/<int:pk>',     ReleaseDetailView.as_view(),        name='release_detail'),
    path('release_create',              ReleaseCreateView.as_view(),        name='release_create'),
    path('release_update/<int:pk>',     ReleaseUpdateView.as_view(),        name='release_update'),
    path('release_delete/<int:pk>',     ReleaseDeleteView.as_view(),        name='release_delete'),

    path('univers_list',                UniversList.as_view(),              name='univers_list'),
    path('univers_detail/<int:pk>',     UniversDetailView.as_view(),        name='univers_detail'),
    path('univers_create',              UniversCreateView.as_view(),        name='univers_create'),
    path('univers_update/<int:pk>',     UniversUpdateView.as_view(),        name='univers_update'),
    path('univers_delete/<int:pk>',     UniversDeleteView.as_view(),        name='univers_delete'),
]

