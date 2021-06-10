import datetime
import json
from django.http.response import HttpResponse
import markdown

from django.conf import settings
from django.contrib import messages
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from urllib.parse import urlparse, parse_qs


from ..models.main import (
    MesejWhatsapp
)


class LoginView(View):

    def get(self, request):
        context = {}    
        return render(request, 'kpdnhep_eaduan_login.html', context) 


class LogoutView(View):

    def get(self, request):   
        return redirect('https://pipeline.com.my')


class ChatroomView(View):

    def get(self, request):
        context = {}    
        return render(request, 'kpdnhep_eaduan_chatroom.html', context)


class DashboardView(View):

    def get(self, request):
        context = {}    
        return render(request, 'kpdnhep_eaduan_dashboard.html', context)


class BantuanView(View):

    def get(self, request):
        context = {}    
        return render(request, 'kpdnhep_eaduan_bantuan.html', context)



class ChatroomListView(View):

    def get(self, request):
        context = {}    
        return render(request, 'kpdnhep_eaduan_dashboard.html', context)


class ChatroomDetailView(View):

    def get(self, request):
        context = {}    
        return render(request, 'kpdnhep_eaduan_dashboard.html', context)


class LaporanListView(View):

    def get(self, request):
        context = {}    
        return render(request, 'kpdnhep_eaduan_dashboard.html', context)


class LaporanDetailView(View):

    def get(self, request):
        context = {}    
        return render(request, 'kpdnhep_eaduan_dashboard.html', context)



class WebhookView(View):

    @csrf_exempt
    def post(self, request):

        data_string = 'https://url.com/asd?' + request.body.decode("utf-8") 
        print(data_string)
        _data = parse_qs(data_string.query)
        print(_data)

        MesejWhatsapp.objects.create(
            message_sid = _data['MessageSid'] ,
            account_sid = _data['AccountSid'] ,
            profile_name = _data['ProfileName'] ,
            body = _data['Body'] ,
            whatsapp_id = _data['WaId']             
        )
        
        return HttpResponse(status=200)


