
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

from helpers.qr import generate_image_qr_from_text

class CorpUserView(View):

    def get(self, request):
        context = {}        
        return render(request, 'jpj_osc/corp_user/dashboard.html', context)      


class CorpUserLesenMemanduView(View):

    def get(self, request):
        context = {}
        return render(request, 'jpj_osc/corp_user/dashboard.html', context)      

    def post(self, request):
        context = {}
        return render(request, 'jpj_osc/corp_user/dashboard.html', context)         

    def put(self, request):
        context = {}
        return render(request, 'jpj_osc/corp_user/dashboard.html', context)    
