import datetime
import json
import markdown

from django.conf import settings
from django.contrib import messages
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View


class LoginView(View):

    def get(self, request):
        context = {}    
        print('OK') 
        return render(request, 'piper_login.html', context) 


class LogoutView(View):

    def get(self, request):   
        print('OK') 
        return redirect('https://pipeline.com.my')


class DashboardView(View):

    def get(self, request):
        context = {}    
        print('OK') 
        return render(request, 'piper_dashboard.html', context)   


class ProjekListView(View):

    def get(self, request):
        context = {}    
        print('OK') 
        return render(request, 'piper_projek_list.html', context) 


class ProjekDetailView(View):

    def get(self, request):
        context = {}    
        print('OK') 
        return render(request, 'piper_projek_detail.html', context)                    


class KerjaListView(View):

    def get(self, request):
        context = {}    
        print('OK') 
        return render(request, 'piper_kerja_list.html', context) 


class KerjaDetailView(View):

    def get(self, request):
        context = {}    
        print('OK') 
        return render(request, 'piper_kerja_detail.html', context) 