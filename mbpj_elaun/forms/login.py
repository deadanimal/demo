from django.forms import ModelForm, Form
from django import forms
from mbpj_elaun.models.login import Login

class LoginForm(Form):

    nric = forms.CharField(label='NRIC', required=True)
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput())
