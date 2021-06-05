from django.forms import ModelForm, Form
from django import forms



class SistemMaintenanceForm(Form):

    elaun_id = forms.UUIDField(widget=forms.HiddenInput())
    buang = forms.BooleanField()


class SistemPendaftaranForm(Form):

    elaun_id = forms.UUIDField(widget=forms.HiddenInput()) 


class SistemSemakanForm(Form):

    elaun_id = forms.UUIDField(widget=forms.HiddenInput())        

