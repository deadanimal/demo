
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from django.http import Http404, JsonResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import routers, serializers, viewsets

from airsel_inventory.viewsets.inbound import (
    APIPurchaseOrderInterfaceViewSet,
    APIMaterialRequestInterfaceViewSet,
    APIItemInterfaceViewSet
)

from airsel_inventory.viewsets.outbound import (
    APIGrnViewSet,
    APIInventoryTransactionViewSet,
    APIMrTransactionViewSet,
    APIMrTransactionChildViewSet
)

# from airsel_inventory.viewsets.outbound import (
#     APIGrnInterfaceInterfaceViewSet,
#     APIGrnInterface2InterfaceViewSet,
#     APIInventoryTransactionInterfaceViewSet,
#     APIInventoryTransactionFromProjectInterfaceViewSet,
#     APIInventoryTransactionFromMaintenanceInterfaceViewSet,
# )

api_router = routers.DefaultRouter()

api_router.register('outbound-grn', APIGrnViewSet, basename='api_outbound_grn')
api_router.register('outbound-inventory-transaction', APIInventoryTransactionViewSet, basename='api__outbound_inventory_transaction')
api_router.register('outbound-mr-transaction', APIMrTransactionViewSet, basename='api__outbound_mr_transaction')
api_router.register('outbound-mr-transaction-child', APIMrTransactionChildViewSet, basename='api__outbound_mr_transaction')


# api_router.register('inbound-purchase-order-interface', APIPurchaseOrderInterfaceViewSet, basename='api_inbound_purchase_order_interface')
# api_router.register('inbound-material-request-interface', APIMaterialRequestInterfaceViewSet, basename='api_inbound_material_request_interface')
# api_router.register('inbound-item-interface', APIItemInterfaceViewSet, basename='api_inbound_item_interface')

# api_router.register('outbound-grn-interface', APIGrnInterfaceInterfaceViewSet, basename='api_outbound_grn_interface')
# api_router.register('outbound-grn2-interface', APIGrnInterface2InterfaceViewSet, basename='api_outbound_grn2_interface')
# api_router.register('outbound-inventory-transaction-interface', APIInventoryTransactionInterfaceViewSet, basename='api_outbound_inventory_transaction_interface')
# api_router.register('outbound-inventory-transaction-from-project-interface', APIInventoryTransactionFromProjectInterfaceViewSet, basename='api_outbound_inventory_transaction_from_project_interface')
# api_router.register('outbound-inventory-transaction-from-maintenance-interface', APIInventoryTransactionFromMaintenanceInterfaceViewSet, basename='api_outbound_inventory_transaction_from_maintenance_interface')
