
from mbpj_elaun.models.login import Login
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

from mbpj_elaun.forms.login import LoginForm

class UserDashboardView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['userGroup'] = request.session['userGroup']            
        
        return render(request, 'mbpj_elaun/dashboard.html', context)      

class UserLoginView(View):

    def get(self, request):
        context = {}
        form = LoginForm()
        context['form'] = form
        return render(request, 'mbpj_elaun/login.html', context)   


    def post(self, request):

        form_ = LoginForm(request.POST)
        if form_.is_valid():
            form_data = form_.cleaned_data
            nric = form_data['nric']
            password = form_data['password']
            # do checking with SSO on password and if ok, proceed, otherwise error
            login = Login.objects.create(nric=nric)
            request.session['nric'] = nric
            request.session['userGroup'] = nric

        return redirect(reverse('mbpj_elaun_dashboard'))   


class UserLogoutView(View):

    def get(self, request):
        request.session.flush()
        if 'nric' in request.session:
            del request.session['nric']
        if 'userGroup' in request.session:
            del request.session['userGroup'] 

        return redirect(reverse('mbpj_elaun_login'))         
        

