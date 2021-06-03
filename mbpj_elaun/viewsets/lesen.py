
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

class APIAccountViewSet(viewsets.ModelViewSet):
    #queryset = Wallet.objects.all()
    #serializer_class = WalletSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny] # IsAuthenticated
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    
         
    def get_queryset(self):
        pass
        #queryset = Wallet.objects.all()            
        #return queryset        