
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View


class DepositListView(View):

    def get(self, request):
        messages.success(request, 'Lol')
        context = {}
        return render(request, 'deposits/list.html', context)

class DepositOnRampFormView(View):

    def get(self, request):
        context = {}
        return render(request, 'deposits/onramp_form.html', context)

    def post(self, request):
        context = {}
        return render(request, 'deposits/onramp_form.html', context)  

class DepositOffRampFormView(View):

    def get(self, request):
        context = {}
        return render(request, 'deposits/offramp_form.html', context)

    def post(self, request):
        context = {}
        return render(request, 'deposits/offramp_form.html', context)                  

class DepositDetailView(View):

    def get(self, request, deposit_id):
        context = {}
        return render(request, 'deposits/main.html', context)      

    def put(self, request, deposit_id):
        context = {}
        return render(request, 'deposits/main.html', context)           
