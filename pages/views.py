
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View


class HomeView(View):

    def get(self, request):
        context = {}
        return render(request, 'pages/home.html', context)