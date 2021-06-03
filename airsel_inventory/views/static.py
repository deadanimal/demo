
from django.shortcuts import render, redirect, reverse
from django.views.generic import View


class HomeView(View):

    def get(self, request):
        context = {}
        return render(request, 'airsel_inventory/home.html', context)       
