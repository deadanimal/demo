
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


class MainView(View):

    def get(self, request):
        auth_user = is_user_login_ok(request)
        if not auth_user:
            login_url = get_login_url(request)
            return redirect(login_url)
        else:
            user_id = auth_user

        context = {
            'userId': user_id
        }
        
        return render(request, 'demo/main.html', context)       




class LogoutView(View):

    def get(self, request):
        redirect_url = request.build_absolute_uri('home')
        url = f"{config('FUSION_AUTH_BASE_URL')}/oauth2/logout?client_id={config('FUSION_AUTH_APP_ID')}"
        return redirect(url)     


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
