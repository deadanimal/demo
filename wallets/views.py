import os
import json


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

from .forms import WalletForm
from .helpers import create_substrate_wallet
from .models import Wallet
from .serializers import WalletSerializer


class WalletListView(View):

    def get(self, request):

        wallet_form = WalletForm()
        wallets = Wallet.objects.all()

        context = {
            'form': wallet_form,
            'wallets': wallets,
        }
        return render(request, 'wallets/list.html', context)

    def post(self, request):

        form = WalletForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data['nickname'])
            form.save()

        wallet_form = WalletForm()
        wallets = Wallet.objects.all()

        context = {
            'form': wallet_form,
            'wallets': wallets
        }
        return render(request, 'wallets/list.html', context)        

class WalletDetailView(View):

    def get(self, request, wallet_id):
        wallet_form = WalletForm()
        wallet = Wallet.objects.filter(id=wallet_id).first()
        
        context = {
            'form': wallet_form,
            'wallet': wallet
        }
        return render(request, 'wallets/detail.html', context)   

    def put(self, request, wallet_id):

        wallet_form = WalletForm()
        wallet = Wallet.objects.filter(id=wallet_id).first()

        context = {
            'form': wallet_form,
            'wallet': wallet
        }
        return render(request, 'wallets/detail.html', context)         

class WalletTransferInView(View):

    def get(self, request):
        context = {}
        return render(request, 'wallets/transfer_in.html', context)  

class WalletTransferOutView(View):

    def get(self, request):
        context = {}
        return render(request, 'wallets/transfer_out.html', context)          

class WalletTransferListView(View):

    def get(self, request, wallet_id):
        context = {}
        return render(request, 'wallets/transfer_list.html', context)   


class WalletTransferDetailView(View):

    def get(self, request, wallet_id, transfer_id):
        context = {}
        return render(request, 'wallets/transfer_detail.html', context)                



class APIWalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny] # IsAuthenticated
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    
         
    def get_queryset(self):
        queryset = Wallet.objects.all()            
        return queryset