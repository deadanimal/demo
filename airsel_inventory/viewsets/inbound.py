
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

from ..models.inbound import PurchaseOrderInterface, MaterialRequestInterface, ItemInterface
from ..serializers.inbound import PurchaseOrderInterfaceSerializer, MaterialRequestInterfaceSerializer, ItemInterfaceSerializer

class APIPurchaseOrderInterfaceViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrderInterface.objects.all()
    serializer_class = PurchaseOrderInterfaceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny] # IsAuthenticated
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    
         
    def get_queryset(self):
        queryset = PurchaseOrderInterface.objects.all()            
        return queryset       


class APIMaterialRequestInterfaceViewSet(viewsets.ModelViewSet):
    queryset = MaterialRequestInterface.objects.all()
    serializer_class = MaterialRequestInterfaceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny] # IsAuthenticated
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    
         
    def get_queryset(self):
        queryset = MaterialRequestInterface.objects.all()            
        return queryset                 

class APIItemInterfaceViewSet(viewsets.ModelViewSet):
    queryset = ItemInterface.objects.all()
    serializer_class = ItemInterfaceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny] # IsAuthenticated
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    
         
    def get_queryset(self):
        queryset = ItemInterface.objects.all()            
        return queryset            