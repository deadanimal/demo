
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


class UserLesenView(View):

    def get(self, request):
        context = {}      
        return render(request, 'jpj_osc/user/lesen.html', context)     

    def post(self, request):
        name = request.POST
        print(name)        
        billplz_ = create_bill(
            'f0a6x07t', # Collection ID
            '+60124290640',  # Mobile number
            300, # RM Amount
            'Ali Shaikh', # Name of User
            'Renewal of license',  # Payment Description
            'http://demoapp.com.my/jpj-osc/webhook-billplz/', # Callback URL
            'http://demoapp.com.my/jpj-osc/user/', # Redirect URL
            'Tujuan', # Reference 1 Label
            'Pembahruan Lesen', # Reference 1 
            'NRIC', # Reference 2 Label
            '800619-01-1497' # Reference 2 
        )
        return redirect(billplz_['url'])      

    def put(self, request):
        context = {}
        return render(request, 'jpj_osc/user/lesen.html', context)   


class UserGeranView(View):

    def get(self, request):
        context = {}    
        return render(request, 'jpj_osc/user/geran.html', context) 

class UserSemakanView(View):

    def get(self, request):
        context = {}    
        return render(request, 'jpj_osc/user/semakan.html', context)         

class UserPlatView(View):

    def get(self, request):
        context = {}    
        return render(request, 'jpj_osc/user/plat.html', context) 

class UserBayaranView(View):

    def get(self, request):
        context = {}    
        return render(request, 'jpj_osc/user/bayaran.html', context)             

    def post(self, request):
        billplz_ = create_bill(
            'f0a6x07t', # Collection ID
            '+60124290640',  # Mobile number
            300, # RM Amount
            'Ali Shaikh', # Name of User
            'Renewal of license',  # Payment Description
            'http://127.0.0.1:8000/jpj-osc/webhook-billplz/', # Callback URL
            'http://127.0.0.1:8000/jpj-osc/user/', # Redirect URL
            'ref1lab', # Reference 1 Label
            'ref1', # Reference 1 
            'ref2lab', # Reference 2 Label
            'ref2' # Reference 2 
        )
        return redirect(billplz_['url'])