
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View


class ChainListView(View):

    def get(self, request):
        context = {}
        return render(request, 'chains/dashboard.html', context)

    def post(self, request):
        context = {}
        return render(request, 'chains/dashboard.html', context)        

class ChainDetailView(View):

    def get(self, request):
        context = {}
        return render(request, 'chains/dashboard.html', context)      

    def put(self, request):
        context = {}
        return render(request, 'chains/dashboard.html', context)            
