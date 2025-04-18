
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


from ..models.outbound import (
    Grn,
    InventoryTransaction,
    MrTransaction,
    MrTransactionChild
)

from ..serializers.outbound import (
    GrnSerializer,
    InventoryTransactionSerializer,
    MrTransactionSerializer,
    MrTransactionChildSerializer
)
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

class APIGrnViewSet(viewsets.ModelViewSet):
    queryset = Grn.objects.all()
    serializer_class = GrnSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny] # IsAuthenticated
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    
         
    def get_queryset(self):
        queryset = Grn.objects.all()            
        return queryset       


class APIInventoryTransactionViewSet(viewsets.ModelViewSet):
    queryset = InventoryTransaction.objects.all()
    serializer_class = InventoryTransactionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny] # IsAuthenticated
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    
         
    def get_queryset(self):
        queryset = InventoryTransaction.objects.all()            
        return queryset                 

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


class APIMrTransactionViewSet(viewsets.ModelViewSet):
    queryset = MrTransaction.objects.all()
    serializer_class = MrTransactionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny] # IsAuthenticated
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    
         
    def get_queryset(self):
        queryset = MrTransaction.objects.all()            
        return queryset  

class APIMrTransactionChildViewSet(viewsets.ModelViewSet):
    queryset = MrTransactionChild.objects.all()
    serializer_class = MrTransactionChildSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny] # IsAuthenticated
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    
         
    def get_queryset(self):
        queryset = MrTransactionChild.objects.all()            
        return queryset          