# coding: utf8
"""
URLS
"""
from django.urls import path

from .views import TeamList, TeamDetailView, TeamCreateView, TeamUpdateView, TeamDeleteView
from .views import PersonList, PersonDetailView, PersonCreateView, PersonUpdateView, PersonDeleteView


urlpatterns = [
    path('team_list',            TeamList.as_view(),          name='team_list'),
    path('team_detail/<int:pk>', TeamDetailView.as_view(),    name='team_detail'),
    path('team_create/',         TeamCreateView.as_view(),    name='team_create'),
    path('team_update/<int:pk>', TeamUpdateView.as_view(),    name='team_update'),
    path('team_delete/<int:pk>', TeamDeleteView.as_view(),    name='team_delete'),
    
    path('person_list',            PersonList.as_view(),          name='person_list'),
    path('person_detail/<int:pk>', PersonDetailView.as_view(),    name='person_detail'),
    path('person_create/',         PersonCreateView.as_view(),    name='person_create'),
    path('person_update/<int:pk>', PersonUpdateView.as_view(),    name='person_update'),
    path('person_delete/<int:pk>', PersonDeleteView.as_view(),    name='person_delete')
]