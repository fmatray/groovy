# coding: utf8
"""
URLS
"""
from django.urls import path

from .views import TeamList, TeamDetailView, TeamCreateView, TeamUpdateView, TeamDeleteView


urlpatterns = [
    path('team_list',            TeamList.as_view(),          name='team_list'),
    path('team_detail/<int:pk>', TeamDetailView.as_view(),    name='team_detail'),
    path('team_create/',         TeamCreateView.as_view(),    name='team_create'),
    path('team_update/<int:pk>', TeamUpdateView.as_view(),    name='team_update'),
    path('team_delete/<int:pk>', TeamDeleteView.as_view(),    name='team_delete')
]