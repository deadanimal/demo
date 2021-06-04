
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

# from ..models.outbound import (
#     GrnInterfaceInterface,
#     GrnInterface2Interface,
#     InventoryTransactionInterface,
#     InventoryTransactionFromProjectInterface,
#     InventoryTransactionFromMaintenanceInterface
# )
# from ..serializers.outbound import (
#     GrnInterfaceInterfaceSerializer,
#     GrnInterface2InterfaceSerializer,
#     InventoryTransactionInterfaceSerializer,
#     InventoryTransactionFromProjectInterfaceSerializer,
#     InventoryTransactionFromMaintenanceInterfaceSerializer
# )

# class APIGrnInterfaceInterfaceViewSet(viewsets.ModelViewSet):
#     queryset = GrnInterfaceInterface.objects.all()
#     serializer_class = GrnInterfaceInterfaceSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

#     def get_permissions(self):
#         if self.action == 'list':
#             permission_classes = [AllowAny] # IsAuthenticated
#         else:
#             permission_classes = [AllowAny]

#         return [permission() for permission in permission_classes]    
         
#     def get_queryset(self):
#         queryset = GrnInterfaceInterface.objects.all()            
#         return queryset       


# class APIGrnInterface2InterfaceViewSet(viewsets.ModelViewSet):
#     queryset = GrnInterface2Interface.objects.all()
#     serializer_class = GrnInterface2InterfaceSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

#     def get_permissions(self):
#         if self.action == 'list':
#             permission_classes = [AllowAny] # IsAuthenticated
#         else:
#             permission_classes = [AllowAny]

#         return [permission() for permission in permission_classes]    
         
#     def get_queryset(self):
#         queryset = GrnInterface2Interface.objects.all()            
#         return queryset                 

# class APIInventoryTransactionInterfaceViewSet(viewsets.ModelViewSet):
#     queryset = InventoryTransactionInterface.objects.all()
#     serializer_class = InventoryTransactionInterfaceSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

#     def get_permissions(self):
#         if self.action == 'list':
#             permission_classes = [AllowAny] # IsAuthenticated
#         else:
#             permission_classes = [AllowAny]

#         return [permission() for permission in permission_classes]    
         
#     def get_queryset(self):
#         queryset = InventoryTransactionInterface.objects.all()            
#         return queryset       

# class APIInventoryTransactionFromProjectInterfaceViewSet(viewsets.ModelViewSet):
#     queryset = InventoryTransactionFromProjectInterface.objects.all()
#     serializer_class = InventoryTransactionFromProjectInterfaceSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

#     def get_permissions(self):
#         if self.action == 'list':
#             permission_classes = [AllowAny] # IsAuthenticated
#         else:
#             permission_classes = [AllowAny]

#         return [permission() for permission in permission_classes]    
         
#     def get_queryset(self):
#         queryset = InventoryTransactionFromProjectInterface.objects.all()            
#         return queryset                 

# class APIInventoryTransactionFromMaintenanceInterfaceViewSet(viewsets.ModelViewSet):
#     queryset = InventoryTransactionFromMaintenanceInterface.objects.all()
#     serializer_class = InventoryTransactionFromMaintenanceInterfaceSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

#     def get_permissions(self):
#         if self.action == 'list':
#             permission_classes = [AllowAny] # IsAuthenticated
#         else:
#             permission_classes = [AllowAny]

#         return [permission() for permission in permission_classes]    
         
#     def get_queryset(self):
#         queryset = InventoryTransactionFromMaintenanceInterface.objects.all()            
#         return queryset                     