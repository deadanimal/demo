import json
from django.conf import settings
from django.contrib import messages

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from django.http import Http404, JsonResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from helpers.billplz import create_bill
from helpers.qr import generate_image_qr_from_text

from ..models.outbound import (
    Grn,
    InventoryTransaction
)


class OutboundView(View):

    def get(self, request):
        request.GET

        from_date = request.GET['from_date']
        to_date = request.GET['to_date']
        interface = request.GET['interface']
        business = request.GET['business']

        if interface == 'GRNTransactions':
            data_ = Grn.objects.all()
        elif interface == 'InventoryTransactions':
            data_ = InventoryTransaction.objects.all()

        empty_ = []
        for item in data_:
            empty_.append(item)

        return JsonResponse(empty_, safe=False)

