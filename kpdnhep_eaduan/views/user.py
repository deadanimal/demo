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


from ..dummy.message import (
    basic_reply
)

from ..helpers.message import (
    send_message
)

from ..models.main import (
    MesejWhatsapp,
    Aduan,
    Bantuan,
    Chatroom,
    ChatroomMesej

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




class BantuanListView(View):

    def get(self, request):
        context = {}    
        return render(request, 'kpdnhep_eaduan_dashboard.html', context)


class BantuanDetailView(View):

    def get(self, request):
        context = {}    
        return render(request, 'kpdnhep_eaduan_dashboard.html', context)



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

        url = 'https://url.com/asd?' + request.body.decode("utf-8") 
        parsed_url = urlparse(url)
        _data = parse_qs(parsed_url.query)

        message_sid = _data['MessageSid'][0]
        account_sid = _data['AccountSid'][0]
        profile_name = _data['ProfileName'][0]
        body = _data['Body'][0]
        whatsapp_id = _data['WaId'][0]

        aduan = '#TAMAT'
        semak = '#SEMAK'
        faq = '#FAQ'
        change_language_bm = '#TUKARBM'
        change_language_en = '#TUKAREN'
        chat_ = '#CHAT'
        
        if aduan in body:
            send_message(whatsapp_id, "Reply by KPDNHEP representative will arrive soon.")   
            aduan = Aduan.objects.create(whatsapp_id=whatsapp_id)
        elif semak in body:
            send_message(whatsapp_id, "Number semakan adalah")   
        elif faq in body:
            send_message(whatsapp_id, "Message FAQ adalah")   
        elif change_language_bm in body:
            send_message(whatsapp_id, "Bahasa ditukar ke Bahasa Malaysia")   
        elif change_language_en in body:
            send_message(whatsapp_id, "Language changed to English")   
        elif chat_ in body:
            chatroom = Chatroom.objects.get_or_create(whatsapp_id=whatsapp_id)              
            ChatroomMesej.objects.create(
                chatroom = chatroom.id,
                body=body
            )
        else:
            send_message(whatsapp_id, basic_reply)     


        MesejWhatsapp.objects.create(
            message_sid = message_sid,
            account_sid = account_sid,
            profile_name = profile_name,
            body = body,
            whatsapp_id = whatsapp_id
        )
        
        return HttpResponse(status=200)


