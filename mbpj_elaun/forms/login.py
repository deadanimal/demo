from django.forms import ModelForm, Form
from django import forms
from ..models.login import Login

class LoginForm(Form):

    nric = forms.CharField(label='Kad Pengenalan', required=True)
    password = forms.CharField(label='Kata Laluan', required=True, widget=forms.PasswordInput())


class TukarPasswordForm(Form):

    nric = forms.CharField(label='')
    password_lama = forms.CharField(label='Kata Laluan Lama', required=True, widget=forms.PasswordInput())
    password_baru_1 = forms.CharField(label='Kata Laluan Baru', required=True, widget=forms.PasswordInput())
    password_baru_2 = forms.CharField(label='Kata Laluan Baru (Ulang)', required=True, widget=forms.PasswordInput())
