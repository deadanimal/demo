
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

from airsel_inventory.viewsets.inbound import APIPurchaseOrderInterfaceViewSet, APIMaterialRequestInterfaceViewSet, APIItemInterfaceViewSet

api_router = routers.DefaultRouter()

api_router.register('inbound-purchase-order-interface', APIPurchaseOrderInterfaceViewSet, basename='api_purchase_order_interface')
api_router.register('inbound-material-request-interface', APIMaterialRequestInterfaceViewSet, basename='api_material_request_interface')
api_router.register('inbound-item-interface', APIItemInterfaceViewSet, basename='api_item_interface')