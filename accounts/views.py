
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from fusionauth.fusionauth_client import FusionAuthClient

from decouple import config

from accounts.helpers import is_user_login_ok, get_login_url, get_or_create_user


class MainView(View):

    def get(self, request):
        auth_user = is_user_login_ok(request)
        if not auth_user:
            login_url = get_login_url(request)
            return redirect(login_url)
        else:
            user_id = auth_user

        context = {
            'userId': user_id
        }
        
        return render(request, 'accounts/main.html', context)       




class LogoutView(View):

    def get(self, request):
        redirect_url = request.build_absolute_uri('home')
        url = f"{config('FUSION_AUTH_BASE_URL')}/oauth2/logout?client_id={config('FUSION_AUTH_APP_ID')}"
        return redirect(url)     
