# coding: utf8
"""
URLS
"""
from django.urls import path
from django.contrib.auth import views
from .views.index import IndexView
from .views.password import PasswordChangeView
from .views.tags import TagListView, TagView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tag/<slug:slug>', TagView.as_view(), name='tag'),
    path('tags', TagListView.as_view(), name='tag_list'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
]

