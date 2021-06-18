import datetime
import json
import markdown

from django.conf import settings
from django.contrib import messages
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from django.contrib.gis.geos import LineString, Point

from ..models.checkin import Checkin
from ..forms.checkin import CheckinForm


class LoginView(View):

    def get(self, request):
        context = {}    
        return render(request, 'piper_login.html', context) 


class LogoutView(View):

    def get(self, request):   
        return redirect('https://pipeline.com.my')


class DashboardView(View):

    def get(self, request):
        context = {}    
        return render(request, 'piper_dashboard.html', context)   
   

class CheckinListView(View):

    def get(self, request):
        context = {}    

        checkins = Checkin.objects.all()
        checkin_form = CheckinForm()

        context['checkins'] = checkins
        context['checkin_form'] = checkin_form
        return render(request, 'piper_checkin_list.html', context) 

    def post(self, request):
        data = request.POST
        print(data)
        return redirect('piper_checkin_list')


class CheckinDetailView(View):

    def get(self, request, checkin_id):
        context = {}    
        context['checkin'] = Checkin.objects.get(id=checkin_id)
        return render(request, 'piper_checkin_detail.html', context)          


class ProjekListView(View):

    def get(self, request):
        context = {}    
        return render(request, 'piper_projek_list.html', context) 


class ProjekDetailView(View):

    def get(self, request):
        context = {}    
        return render(request, 'piper_projek_detail.html', context)                    


class KerjaListView(View):

    def get(self, request):
        context = {}    
        return render(request, 'piper_kerja_list.html', context) 


class KerjaDetailView(View):

    def get(self, request):
        context = {}    
        return render(request, 'piper_kerja_detail.html', context) 