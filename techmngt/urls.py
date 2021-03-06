# coding: utf8
"""
URLS
"""
from django.urls import path

from .views.asynchronous import AsynchronousFlowList, AsynchronousFlowDetailView, \
    AsynchronousFlowCreateView, AsynchronousFlowUpdateView, AsynchronousFlowDeleteView
from .views.batch import BatchFlowList, BatchFlowDetailView, \
    BatchFlowCreateView, BatchFlowUpdateView, BatchFlowDeleteView
from .views.uri import URIFlowList, URIFlowDetailView, \
    URIFlowCreateView, URIFlowUpdateView, URIFlowDeleteView
from .views.synchronous import SynchronousFlowList, SynchronousFlowDetailView, \
    SynchronousFlowCreateView, SynchronousFlowUpdateView, SynchronousFlowDeleteView

from .views.network import NetworkFlowList, NetworkFlowDetailView, \
    NetworkFlowCreateView, NetworkFlowUpdateView, NetworkFlowDeleteView

from .views.server import ServerList, ServerDetailView, \
    ServerCreateView, ServerUpdateView, ServerDeleteView

urlpatterns = [
    path('asynchronous_list', AsynchronousFlowList.as_view(), name='asynchronousflow_list'),
    path('asynchronous_detail/<int:pk>', AsynchronousFlowDetailView.as_view(), name='asynchronousflow_detail'),
    path('asynchronous_create/', AsynchronousFlowCreateView.as_view(), name='asynchronousflow_create'),
    path('asynchronous_update/<int:pk>', AsynchronousFlowUpdateView.as_view(), name='asynchronousflow_update'),
    path('asynchronous_delete/<int:pk>', AsynchronousFlowDeleteView.as_view(), name='asynchronousflow_delete'),

    path('batch_list', BatchFlowList.as_view(), name='batchflow_list'),
    path('batch_detail/<int:pk>', BatchFlowDetailView.as_view(), name='batchflow_detail'),
    path('batch_create/', BatchFlowCreateView.as_view(), name='batchflow_create'),
    path('batch_update/<int:pk>', BatchFlowUpdateView.as_view(), name='batchflow_update'),
    path('batch_delete/<int:pk>', BatchFlowDeleteView.as_view(), name='batchflow_delete'),

    path('uri_list', URIFlowList.as_view(), name='uriflow_list'),
    path('uri_detail/<int:pk>', URIFlowDetailView.as_view(), name='uriflow_detail'),
    path('uri_create/', URIFlowCreateView.as_view(), name='uriflow_create'),
    path('uri_update/<int:pk>', URIFlowUpdateView.as_view(), name='uriflow_update'),
    path('uri_delete/<int:pk>', URIFlowDeleteView.as_view(), name='uriflow_delete'),
    
    path('synchronous_list', SynchronousFlowList.as_view(), name='synchronousflow_list'),
    path('synchronous_detail/<int:pk>', SynchronousFlowDetailView.as_view(), name='synchronousflow_detail'),
    path('synchronous_create/', SynchronousFlowCreateView.as_view(), name='synchronousflow_create'),
    path('synchronous_update/<int:pk>', SynchronousFlowUpdateView.as_view(), name='synchronousflow_update'),
    path('synchronous_delete/<int:pk>', SynchronousFlowDeleteView.as_view(), name='synchronousflow_delete'),
    
    path('network_list', NetworkFlowList.as_view(), name='networkflow_list'),
    path('network_detail/<int:pk>', NetworkFlowDetailView.as_view(), name='networkflow_detail'),
    path('network_create/', NetworkFlowCreateView.as_view(), name='networkflow_create'),
    path('network_update/<int:pk>', NetworkFlowUpdateView.as_view(), name='networkflow_update'),
    path('network_delete/<int:pk>', NetworkFlowDeleteView.as_view(), name='networkflow_delete'),
    
    path('server_list', ServerList.as_view(), name='server_list'),
    path('server_detail/<int:pk>', ServerDetailView.as_view(), name='server_detail'),
    path('server_create/', ServerCreateView.as_view(), name='server_create'),
    path('server_update/<int:pk>', ServerUpdateView.as_view(), name='server_update'),
    path('server_delete/<int:pk>', ServerDeleteView.as_view(), name='server_delete'),
]
