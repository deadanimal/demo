
from mbpj_elaun.models.login import Login
from django.conf import settings
from django.contrib import messages

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.http import JsonResponse


from accounts.helpers import is_user_login_ok, get_login_url, get_or_create_user


import json



class ApiTokenView(View):

    def get(self, request):
        data = {}          
        if 'Authorization' in request.META:
            pass # create new token
        else:
            data['message'] = 'Authorization Token Not Provided'
        
        return JsonResponse(data)    

    def post(self, request):
        data = {}          
        incoming = json.loads(request.body)

        
        return JsonResponse(data)
