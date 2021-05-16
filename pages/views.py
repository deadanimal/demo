
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View


class HomeView(View):

    def get(self, request):
        context = {}
        return render(request, 'pages/home.html', context)

class AboutView(View):

    def get(self, request):
        context = {}
        return render(request, 'pages/about.html', context)        

class AmlView(View):

    def get(self, request):
        context = {}
        return render(request, 'pages/aml.html', context)  

class ChainView(View):

    def get(self, request):
        context = {}
        return render(request, 'pages/chain.html', context)     

class DeveloperView(View):

    def get(self, request):
        context = {}
        return render(request, 'pages/developer.html', context)         

class EcosystemView(View):

    def get(self, request):
        context = {}
        return render(request, 'pages/ecosystem.html', context)                      

class PrivacyView(View):

    def get(self, request):
        context = {}
        return render(request, 'pages/privacy.html', context)            

class TermsView(View):

    def get(self, request):
        context = {}
        return render(request, 'pages/terms.html', context)                   
