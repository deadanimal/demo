import datetime
import json
import markdown

from django.conf import settings
from django.contrib import messages
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View


class HomeView(View):

    def get(self, request):
        context = {}    
        print('OK') 
        return render(request, 'bootcamp_home.html', context)      

    def post(self, request):
        context = {}     
        return render(request, 'bootcamp_home.html', context)         


class AdminView(View):

    def get(self, request):
        context = {}     
        return render(request, 'bootcamp_admin.html', context)      

    def post(self, request):
        context = {}     
        return render(request, 'bootcamp_admin.html', context)       



class DeveloperDayListView(View):

    def get(self, request, day=None):
        context = {}     
        with open('bootcamp/dummy/developer_day.json') as f:
            data = json.load(f)        
        context['days'] = data['listOfDays']
        return render(request, 'bootcamp_developer_day_list.html', context)      

    def post(self, request):
        context = {}     
        return True  


class DeveloperDayDetailView(View):

    def get(self, request, day):
        context = {}
        
        with open('bootcamp/dummy/developer_day.json') as f:
            data = json.load(f)        
        context['day'] = data['listOfDays'][day-1]

        file_name = 'bootcamp/notes/developer_day_' + str(day) +'.md'             
        with open(file_name) as f:
            text = f.read()           
        html_note = markdown.markdown(text)
        context['html_note'] = html_note

        return render(request, 'bootcamp_developer_day_detail.html', context)      

    def post(self, request):
        context = {}     
        return True                 

# class LoginView(View):

#     def get(self, request):
#         context = {}
#         form = LoginForm()
#         context['form'] = form
#         return render(request, 'bootcamp_login.html', context)   


#     def post(self, request):

#         with open('mbpj_elaun/dummy/user.json') as f:
#             data = json.load(f)

#         form_ = LoginForm(request.POST)
#         if form_.is_valid():
#             form_data = form_.cleaned_data
#             nric = form_data['nric']
#             password = form_data['password']
#             # do checking with SSO on password and if ok, proceed, otherwise error
            
#             login = Login.objects.create(nric=nric)

#             for item in data:
#                 if item['nric'] == nric:
#                     print('Same NRIC')
#                     request.session['user'] = item

#             request.session['nric'] = nric
#             request.session['userGroup'] = nric

#         return redirect(reverse('mbpj_elaun_dashboard'))   


# class LogoutView(View):

#     def get(self, request):
#         request.session.flush()
#         if 'nric' in request.session:
#             del request.session['nric']
#         if 'user' in request.session:
#             del request.session['user']
#         if 'userGroup' in request.session:
#             del request.session['userGroup']              

#         return redirect(reverse('mbpj_elaun_login'))         
        

