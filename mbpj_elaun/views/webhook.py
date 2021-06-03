
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View


class BillplzWebhookView(View):

    def post(self, request):
        print(request)
        return 'OK'