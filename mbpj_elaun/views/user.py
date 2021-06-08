import datetime
import json

from django.conf import settings
from django.contrib import messages
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from helpers.billplz import create_bill
from helpers.qr import generate_image_qr_from_text


from ..forms.elaun import (
    ElaunMohonForm,
)

from ..forms.login import (
    LoginForm,
    TukarPasswordForm
)

from ..models.elaun import (
    Elaun,
    ElaunPerson
)

from ..models.login import (
    Login
)

class UserDashboardView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']      

        if context['user']['noPekerja'] == '1':
            elaun = Elaun.objects.filter(elaunperson__in=ElaunPerson.objects.filter(nric=context['nric']))
        else:
            elaun = Elaun.objects.all()    
        context['elauns'] = elaun              
        
        return render(request, 'mbpj_elaun_dashboard.html', context)      

class UserLoginView(View):

    def get(self, request):
        context = {}
        form = LoginForm()
        context['form'] = form
        return render(request, 'mbpj_elaun_login.html', context)   


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
        elaun = Elaun.objects.filter(elaunperson__in=ElaunPerson.objects.filter(nric=context['nric']))
        context['elauns'] = elaun
        
        return render(request, 'mbpj_elaun_elaun_mohon.html', context)

    def post(self, request):
        form = ElaunMohonForm(request.POST)

        elaun = Elaun.objects.create(
            status= '00',
            jenis_permohonan = form.data['jenis_permohonan'],
            tarikh_mula = form.data['tarikh_mula'],
            tarikh_akhir = form.data['tarikh_akhir'],
            sebab_lebih_masa = form.data['sebab_lebih_masa'],
            lokasi = form.data['lokasi'],
            pegawai_lulus = form.data['pegawai_lulus'],
            pegawai_sah = form.data['pegawai_sah'],
        )
        masa_mula = datetime.datetime.strptime(elaun.tarikh_mula, "%Y-%m-%dT%H:%M")
        masa_akhir = datetime.datetime.strptime(elaun.tarikh_akhir, "%Y-%m-%dT%H:%M")
        elaun.masa = masa_akhir - masa_mula
        elaun.save()
        ElaunPerson.objects.create(
            nric = form.data['pemohon_nric'],
            kod_pekerja = form.data['pemohon_kod_pekerja'],
            elaun = elaun
        )        
        if form.data['jenis_permohonan'] == 'A2':
            print(form.data)
            count = int(form.data['count'])
            for item in range(1, count+1):
                form_statement = 'noPekerja' + str(item)
                person_tambahan = form.data[form_statement]
                ElaunPerson.objects.create(
                    kod_pekerja = person_tambahan,
                    pemohon = False,
                    elaun = elaun
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

        elauns = Elaun.objects.filter(pegawai_lulus=context['user']['noPekerja'])
        context['elauns'] = elauns                
        
        return render(request, 'mbpj_elaun_elaun_lulus.html', context)        


class UserSahView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup'] 

        elauns = Elaun.objects.filter(pegawai_sah=context['user']['noPekerja'])
        for elaun in elauns:
            elaun_persons = ElaunPerson.objects.filter(elaun=elaun)
            for person in elaun_persons:
                if person.pemohon:
                    elaun.pemohon = person.kod_pekerja
        context['elauns'] = elauns     

        return render(request, 'mbpj_elaun_elaun_sah.html', context)        

    def post(self, request): 
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']   

        elaun_id = request.POST['elaun_id']
        elaun = Elaun.objects.get(id=elaun_id)
        if request.POST['sah'] == 'on':
            elaun.pegawai_sah = True
        else:
            elaun.pegawai_sah = False
        elaun.pegawai_sah_catatan = request.POST['nota']
        elaun.save()
        
        return redirect(reverse('mbpj_elaun_sah'))             

class UserTuntutView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun_elaun_tuntut.html', context)                 
                      

class UserPeriksaView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun_finance_periksa.html', context)          


class UserPindaanView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun_finance_pindaan.html', context)                                         


class UserSemakanView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun_finance_semakan.html', context)                                                 

class UserPengurusanView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun_sistem_pengurusan.html', context)                                                         


class UserPendaftaranView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun_sistem_pendaftaran.html', context)        

class UserMaintenanceView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun_sistem_maintenance.html', context)        


class UserBantuanView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun_bantuan.html', context)                


class UserLaporanView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']             
        
        return render(request, 'mbpj_elaun_laporan.html', context)              


class UserProfilView(View):

    def get(self, request):
        context = {}
        if request.session.get('nric') == None:
            return redirect(reverse('mbpj_elaun_login'))

        context['nric'] = request.session['nric']
        context['user'] = request.session['user'] 
        context['userGroup'] = request.session['userGroup']    
        context['form'] = TukarPasswordForm()
        
        return render(request, 'mbpj_elaun_profil.html', context)           

    def post(self, request):

        form = TukarPasswordForm(request.POST)
        if form.is_valid():
            print(form)
            # Change password here...
        else:
            print(form.errors)

        return redirect(reverse('mbpj_elaun_profil'))
