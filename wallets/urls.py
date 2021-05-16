from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.WalletListView.as_view(), name='wallet_list'),
    path('<uuid:wallet_id>/', views.WalletDetailView.as_view(), name='wallet_detail'),
    path('in', views.WalletTransferInView.as_view(), name='wallet_transfer_in'),
    path('out', views.WalletTransferOutView.as_view(), name='wallet_transfer_out'),    
    path('<uuid:wallet_id>/transfers/', views.WalletTransferListView.as_view(), name='wallet_transfer_list'),
    path('<uuid:wallet_id>/transfers/<uuid:transfer_id>', views.WalletTransferListView.as_view(), name='wallet_transfer_detail'),
    
]