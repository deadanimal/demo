
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

class UserDashboardView(View):

    def get(self, request):
        context = {}
        user_json = {
            'status': 'Aktif',
            'expiry': '20 Jun 2022',
            'kelas': ['B','D'],
            'kejara': 30,            
            'nric': '800619-01-1497',
            'name': 'Mohamad Ali bin Shaikh Maidin',
            'address': 'No. 2, Jalan Syed Hassan, Taman Mengkudu, Alor Setar 01000, Kedah',
            'phone': '+60126447890',
        }
        context['user'] = user_json
        context['userQR'] = generate_image_qr_from_text(str(user_json))
        
        return render(request, 'jpj_osc/user/dashboard.html', context)      
