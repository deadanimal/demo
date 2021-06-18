from django.forms import ModelForm, Form
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django import forms

from ..models.checkin import (
    Checkin
)

class CheckinForm(Form):

    user = forms.UUIDField(widget=forms.HiddenInput())
    sebab_lebih_masa = forms.CharField(label="Sebab Lebih Masa")

    # class Meta:
    #     model = Checkin
    #     fields = '__all__'
    #     read_only_fields = ['id']

# class ElaunMohonForm(Form):

#     pemohon_nric = forms.CharField(widget=forms.HiddenInput())
#     pemohon_no_pekerja = forms.CharField(widget=forms.HiddenInput())
#     pemohon_nama = forms.CharField(widget=forms.HiddenInput())
    
#     jenis_permohonan = forms.ChoiceField(
#         label="Jenis Permohonan",
#         choices=(
#             ('A1', 'Persendirian'),
#             ('A2', 'Berkumpulan'),
#         )
#     )
#     tarikh_mula = forms.DateField(
#         label="Tarikh Mula",
#         widget=forms.TextInput(     
#             attrs={'type': 'date'} 
#         )        
#     )    
#     tarikh_akhir = forms.DateField(
#         label="Tarikh Akhir",
#         widget=forms.TextInput(     
#             attrs={'type': 'date'} 
#         )        
#     )        
#     masa_mula = forms.TimeField(
#         label="Masa Mula",
#         widget=forms.TextInput(     
#             attrs={'type': 'time'} 
#         )        
#     )
#     masa_akhir = forms.TimeField(
#         label="Masa Akhir",
#         widget=forms.TextInput(     
#             attrs={'type': 'time'} 
#         )        
#     )
#     sebab_lebih_masa = forms.CharField(label="Sebab Lebih Masa")
#     lokasi = forms.CharField(label="Lokasi")
#     pegawai_lulus = forms.CharField(label="Pegawai Pelulus")
#     pegawai_sah = forms.CharField(label="Pegawai Pengesah")


# class ElaunSahForm(Form):

#     elaun_id = forms.UUIDField(widget=forms.HiddenInput())


# class ElaunLulusForm(Form):

#     elaun_id = forms.UUIDField(widget=forms.HiddenInput()) 


# class ElaunTuntutanForm(Form):

#     elaun_id = forms.UUIDField(widget=forms.HiddenInput())        


# class ElaunKesIstimewaForm(Form):

#     nric = forms.CharField(label='NRIC', required=True)    

