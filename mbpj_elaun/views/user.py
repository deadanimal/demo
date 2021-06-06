
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


import json


from helpers.billplz import create_bill
from helpers.qr import generate_image_qr_from_text

from mbpj_elaun.forms.elaun import (
    ElaunMohonForm,
)

from mbpj_elaun.forms.login import (
    LoginForm,
    TukarPasswordForm
)

from mbpj_elaun.models.elaun import (
    Elaun,
    ElaunPerson
)

class UserDashboardView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']            
        
        return render(request, 'mbpj_elaun/dashboard.html', context)      

class UserLoginView(View):

    def get(self, request):
        context = {}
        form = LoginForm()
        context['form'] = form
        return render(request, 'mbpj_elaun/login.html', context)   


    def post(self, request):

        with open('mbpj_elaun/dummy/user.json') as f:
            data = json.load(f)

        form_ = LoginForm(request.POST)
        if form_.is_valid():
            form_data = form_.cleaned_data
            nric = form_data['nric']
            password = form_data['password']
            # do checking with SSO on password and if ok, proceed, otherwise error
            
            login = Login.objects.create(nric=nric)

            for item in data:
                if item['nric'] == nric:
                    print('Same NRIC')
                    request.session['user'] = item

            request.session['nric'] = nric
            request.session['userGroup'] = nric

        return redirect(reverse('mbpj_elaun_dashboard'))   


class UserLogoutView(View):

    def get(self, request):
        request.session.flush()
        if 'nric' in request.session:
            del request.session['nric']
        if 'user' in request.session:
            del request.session['user']
        if 'userGroup' in request.session:
            del request.session['userGroup']              

        return redirect(reverse('mbpj_elaun_login'))         
        

class UserMohonView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']  
        context['form'] = ElaunMohonForm()       
        elaun = Elaun.objects.all()
        context['elauns'] = elaun
        
        return render(request, 'mbpj_elaun/elaun_mohon.html', context)

    def post(self, request):
        form = ElaunMohonForm(request.POST)
        print(form.data['jenis_permohonan'])
        elaun = Elaun.objects.create(
            jenis_permohonan = form.data['jenis_permohonan'],
            tarikh_mula = form.data['tarikh_mula'],
            tarikh_akhir = form.data['tarikh_akhir'],
            masa_mula = form.data['masa_mula'],
            masa_akhir = form.data['masa_akhir'],
            sebab_lebih_masa = form.data['sebab_lebih_masa'],
            lokasi = form.data['lokasi'],
            pegawai_lulus = form.data['pegawai_lulus'],
            pegawai_sah = form.data['pegawai_sah'],
        )
        return redirect(reverse('mbpj_elaun_mohon'))


class UserLulusView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun/elaun_lulus.html', context)        


class UserSahView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun/elaun_sah.html', context)        

    def post(self, request): 
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun/elaun_sah.html', context)             

class UserTuntutView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun/elaun_tuntut.html', context)                 

class UserKesIstimewaView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun/elaun_kes_istimewa.html', context)                         

class UserPeriksaView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun/finance_periksa.html', context)          


class UserPindaanView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun/finance_pindaan.html', context)                                         


class UserSemakanView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun/finance_semakan.html', context)                                                 

class UserPengurusanView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun/sistem_pengurusan.html', context)                                                         


class UserPendaftaranView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun/sistem_pendaftaran.html', context)        

class UserMaintenanceView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun/sistem_maintenance.html', context)        


class UserBantuanView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun/bantuan.html', context)                


class UserLaporanView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun/laporan.html', context)              


class UserProfilView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']    
        context['form'] = TukarPasswordForm()
        
        return render(request, 'mbpj_elaun/profil.html', context)           

    def post(self, request):

        form = TukarPasswordForm(request.POST)
        if form.is_valid():
            print(form)
        else:
            print(form.errors)

        return redirect(reverse('mbpj_elaun_profil'))
