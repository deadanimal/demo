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
    basic_reply,
    faq_reply
)

from ..helpers.message import (
    send_message
)

from ..models.main import (
    Laporan,
    MesejWhatsapp,
    Aduan,
    Bantuan,
    Chatroom,
    ChatroomMesej,
    Laporan
)


class LoginView(View):

    def get(self, request):
        context = {}    
        return render(request, 'kpdnhep_eaduan_login.html', context) 


class LogoutView(View):

    def get(self, request):   
        return redirect('https://pipeline.com.my')



class DashboardView(View):

    def get(self, request):
        context = {}    
        return render(request, 'kpdnhep_eaduan_dashboard.html', context)


class AduanListView(View):

    def get(self, request):

        context = {}   
        context['aduans'] = Aduan.objects.all() 
        return render(request, 'kpdnhep_eaduan_aduan_list.html', context)


class AduanDetailView(View):

    def get(self, request, aduan_id):
        aduan = Aduan.objects.get(id=aduan_id)
        if 'action' in request.GET:
            if request.GET['action'] == 'tugas':
                aduan.tugas = True
                aduan.save()
                Chatroom.objects.create(
                    whatsapp_id=aduan.whatsapp_id,
                    active=True
                )
                return redirect('kpdnhep_eaduan_chatroom_list')     
            elif request.GET['action'] == 'buang':
                aduan.delete()
                return redirect('kpdnhep_eaduan_aduan_list')     

        context = {}    
        context['aduan'] = aduan
        return render(request, 'kpdnhep_eaduan_aduan_detail.html', context)



class BantuanListView(View):

    def get(self, request):
        context = {}   
        context['bantuans'] = Bantuan.objects.all() 
        return render(request, 'kpdnhep_eaduan_bantuan_list.html', context)


class BantuanDetailView(View):

    def get(self, request, bantuan_id):
        context = {}    
        context['bantuan'] = Bantuan.objects.get(id=bantuan_id)
        return render(request, 'kpdnhep_eaduan_bantuan_detail.html', context)



class ChatroomListView(View):

    def get(self, request):
        context = {}    
        context['chatrooms'] = Chatroom.objects.all()
        
        return render(request, 'kpdnhep_eaduan_chatroom_list.html', context)


class ChatroomDetailView(View):

    def get(self, request, chatroom_id):
        context = {}    
        chatroom = Chatroom.objects.filter(id=chatroom_id).first()
        if chatroom:
            context['chatroom'] = chatroom
            context['wamessages'] = MesejWhatsapp.objects.filter(whatsapp_id=chatroom.whatsapp_id)
            return render(request, 'kpdnhep_eaduan_chatroom_detail.html', context)
        else:
            return redirect('kpdnhep_eaduan_chatroom_list')

    def post(self, request, chatroom_id):
        data = request.POST
        mesej = data['mesej']
        whatsapp_id = data['whatsapp_id']
        MesejWhatsapp.objects.create(
            message_sid = 'KPDNHEP',
            whatsapp_id = whatsapp_id,
            body = mesej
        )
        send_message(whatsapp_id, mesej)
        return redirect('kpdnhep_eaduan_chatroom_detail', chatroom_id= chatroom_id)


class LaporanListView(View):

    def get(self, request):
        context = {}    
        context['laporans'] = Laporan.objects.all()
        return render(request, 'kpdnhep_eaduan_laporan_list.html', context)


class LaporanDetailView(View):

    def get(self, request, laporan_id):
        context = {}    
        context['laporan'] = Laporan.objects.get(id=laporan_id)
        return render(request, 'kpdnhep_eaduan_laporan_detail.html', context)



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
            aduan = Aduan.objects.create(
                whatsapp_id=whatsapp_id,
                body=body                
            )
        elif semak in body:
            send_message(whatsapp_id, "Number semakan adalah.... Template semakan diperlukan")   
        elif faq in body:
            send_message(whatsapp_id, faq_reply)   
        elif change_language_bm in body:
            send_message(whatsapp_id, "Bahasa ditukar ke Bahasa Malaysia")   
        elif change_language_en in body:
            send_message(whatsapp_id, "Language changed to English, template in English is required...")   
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


