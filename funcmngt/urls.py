# coding: utf8
"""
URLS
"""
from django.urls import path

from .views.funcflow import FuncFlowList, FuncFlowDetailView, \
    FuncFlowCreateView, FuncFlowUpdateView, FuncFlowDeleteView
from .views.subfuncflow import SubFuncFlowList, SubFuncFlowDetailView, \
    SubFuncFlowCreateView, SubFuncFlowUpdateView, SubFuncFlowDeleteView


urlpatterns = [
    path('funcflow_list',            FuncFlowList.as_view(),          name='funcflow_list'),
    path('funcflow_detail/<int:pk>', FuncFlowDetailView.as_view(),    name='funcflow_detail'),
    path('funcflow_create/',         FuncFlowCreateView.as_view(),    name='funcflow_create'),
    path('funcflow_update/<int:pk>', FuncFlowUpdateView.as_view(),    name='funcflow_update'),
    path('funcflow_delete/<int:pk>', FuncFlowDeleteView.as_view(),    name='funcflow_delete'),

    path('subfuncflow_list',            SubFuncFlowList.as_view(),       name='subfuncflow_list'),
    path('subfuncflow_detail/<int:pk>', SubFuncFlowDetailView.as_view(), name='subfuncflow_detail'),
    path('subfuncflow_create/',         SubFuncFlowCreateView.as_view(), name='subfuncflow_create'),
    path('subfuncflow_update/<int:pk>', SubFuncFlowUpdateView.as_view(), name='subfuncflow_update'),
    path('subfuncflow_delete/<int:pk>', SubFuncFlowDeleteView.as_view(), name='subfuncflow_delete'),

]