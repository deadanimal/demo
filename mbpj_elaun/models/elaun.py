from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Elaun(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    jenis_permohonan = models.CharField(max_length=255, null=False)
    masa_mula = models.CharField(max_length=255, null=False)
    masa_akhir = models.CharField(max_length=255, null=False)

    sebab_lebih_masa = models.CharField(max_length=255, null=False)
    lokasi = models.CharField(max_length=255, null=False)
    pegawai_pelulus = models.CharField(max_length=255, null=False)

    hari =  models.CharField(max_length=255, null=False)
    waktu =  models.CharField(max_length=255, null=False)
    kadar_jam =  models.CharField(max_length=255, null=False)
    tujuan =  models.CharField(max_length=255, null=False)

    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id

class ElaunPerson(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nric = models.CharField(max_length=255, null=False)
    kod_pekerja = models.CharField(max_length=255, null=False)
    elaun = models.ForeignKey(Elaun, on_delete=models.CASCADE, null=False)

    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id    
        