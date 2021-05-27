
from django.conf import settings
from django.contrib import messages

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View

class LolView(View):

    def get(self, request):
        context = {}

        
        return render(request, 'hsn_main/dashboard.html', context)      