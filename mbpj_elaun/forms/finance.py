from django.forms import ModelForm, Form
from django import forms



class FinancePeriksaForm(Form):

    elaun_id = forms.UUIDField(widget=forms.HiddenInput())


class FinancePindaanForm(Form):

    elaun_id = forms.UUIDField(widget=forms.HiddenInput()) 


class FinanceSemakanForm(Form):

    elaun_id = forms.UUIDField(widget=forms.HiddenInput())        

