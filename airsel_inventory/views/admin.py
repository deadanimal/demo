
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


from fusionauth.fusionauth_client import FusionAuthClient

from decouple import config

from accounts.helpers import is_user_login_ok, get_login_url, get_or_create_user

from helpers.qr import generate_image_qr_from_text


# class AdminView(View):

#     def get(self, request):
#         context = {}
#         return render(request, 'airsel_inventory/admin/dashboard.html', context)  


# class AdminLesenMemanduView(View):

#     def get(self, request):
#         context = {}
#         return render(request, 'airsel_inventory/admin/lesen.html', context)    

#     def post(self, request):
#         context = {}
#         return render(request, 'airsel_inventory/admin/lesen.html', context)           

#     def put(self, request):
#         context = {}
#         return render(request, 'airsel_inventory/admin/lesen.html', context)                    


# class AdminLesenKenderaanPersendirianView(View):

#     def get(self, request):
#         context = {}
#         return render(request, 'airsel_inventory/admin/lesen.html', context)     

#     def post(self, request):
#         context = {}
#         return render(request, 'airsel_inventory/admin/lesen.html', context)        

#     def put(self, request):
#         context = {}
#         return render(request, 'airsel_inventory/admin/lesen.html', context)    


                                        
