from django.urls import path

from . import views

urlpatterns = [
    path('', views.ChainListView.as_view(), name='chain_list'),
    path('<uuid:chain_id>/', views.ChainDetailView.as_view(), name='chain_detail'),
]