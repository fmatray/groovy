# coding: utf8
"""
URLS
"""
from django.urls import path
from django.contrib.auth import views
from .views.index import IndexView
from .views.password import PasswordChangeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
]

