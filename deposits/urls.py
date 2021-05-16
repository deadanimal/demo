from django.urls import path

from . import views

urlpatterns = [
    path('', views.DepositListView.as_view(), name='deposit_list'),
    path('<uuid:deposit_id>/', views.DepositDetailView.as_view(), name='deposit_detail'),
    path('on', views.DepositOnRampFormView.as_view(), name='deposit_onramp_form'),
    path('off', views.DepositOffRampFormView.as_view(), name='deposit_offramp_form'),
]