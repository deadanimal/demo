
from django.conf import settings
from django.contrib import messages

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

from accounts.helpers import is_user_login_ok, get_login_url, get_or_create_user

from helpers.billplz import create_bill
from helpers.qr import generate_image_qr_from_text

class AdminInventoryDashboardView(View):

    def get(self, request):
        context = {}
        return render(request, 'airsel_inventory/admin_inventory/dashboard.html', context)   



# class AdminInventoryDashboardView(View):

#     def get(self, request):
#         context = {}
#         return render(request, 'airsel_inventory/admin_inventory/dashboard.html', context)           

# Stock Receive/Return: Receive PO from ERP
# Stock Receive/Return: Send Details on Receive to StoreKepper
# Stock Receive/Return: Receive Return Issue from StoreKepper
# Stock Receive/Return: Send Return Issue to Supplier
# Stock Receive/Return: Send Updated Return Details to ERP
# Stock Receive/Return: Receive Update from StoreKeeper
# Stock Receive/Return: Close PO
# Stock Receive/Return: Send Updated Inventory to ERP

# Stock Issuance: Receive Issueance from ERP
# Stock Issuance: Receive Stock Details from StoreKeeper
# Stock Issuance: Send Updated Stock Details to ERP
# Stock Issuance: Receive Update from StoreKepper
# Stock Issuance: Send Updated Issuance to ERP

# Interwarehouse Transfer: Receive Request from StoreKeeper
# Interwarehouse Transfer: Update details to be issued
# Interwarehouse Transfer: Send the issue transfer to StoreKeeper
# Interwarehouse Transfer: Receive Record from StoreKeeper
# Interwarehouse Transfer: Send updated transfer details to ERP

# Stock Count: Create Stock Count Task
# Stock Count: Send Stock Count Task to StoreKeeper
# Stock Count: Receive Report from StoreKeeper
# Stock Count: Check Variance on Stock
# Stock Count: Send Variance on Stock to Other Admin
# Stock Count: Update Reject Status on Stock by Other Admin
# Stock Count: Update Variance on Stock by Other Admin
# Stock Count: Monthly Calculation on Stock Variance
# Stock Count: Yearly Calculation on Stock Variance

# Subinventory Transfer: Receive Task Transfer from StoreKeeper
# Subinventory Transfer: Send Task Transfer to ERP

# Item Creation: Receive Data Migration from ERP
# Item Creation: Receive Updated Item from ERP