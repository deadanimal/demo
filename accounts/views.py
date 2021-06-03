
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

from accounts.helpers import is_user_login_ok, get_login_url, get_user_detail, check_user_login


class HomeView(View):

    def get(self, request):
        context = {}        
        return render(request, 'demo/home.html', context)       

class SupportView(View):

    def get(self, request):
        context = {}
        return render(request, 'demo/support.html', context)


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
   



class LoginView(View):

    def get(self, request):
        login_url = get_login_url(request)
        return redirect(login_url)  



class LogoutView(View):

    def get(self, request):
        request.session.flush()
        #del request.session['userId']
        #del request.session['user']
        redirect_url = request.build_absolute_uri('home')
        url = f"{config('FUSION_AUTH_BASE_URL')}/oauth2/logout?client_id={config('FUSION_AUTH_APP_ID')}"
        return redirect(url)     


class LoginCallbackView(View):

    def get(self, request):
        auth_user = is_user_login_ok(request)
        
        if not auth_user:
            login_url = get_login_url(request)
            return redirect(login_url)
        else:
            user_id = auth_user

        user_ = get_user_detail(user_id)
        request.session['userId'] = user_id
        request.session['user'] = user_


        redirect_url = request.build_absolute_uri(reverse("accounts"))
        return redirect(redirect_url)  
