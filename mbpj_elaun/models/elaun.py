from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Elaun(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    jenis_permohonan = models.CharField(max_length=255, null=False)
    tarikh_mula = models.DateTimeField(max_length=255, null=False)
    tarikh_akhir = models.DateTimeField(max_length=255, null=False)
    masa = models.DurationField(null=True)

    sebab_lebih_masa = models.CharField(max_length=255, null=False)
    lokasi = models.CharField(max_length=255, null=False)

    STATUS = [
        ('00', 'Dalam Permohonan'),
        ('01', 'Menunggu Pengesahan oleh Pegawai Pengesah'),
        ('02', 'Pengesahan Ditolak'),
        ('03', 'Menunggu Kelulusan oleh Pegawai Pelulus'),
        ('04', 'Kelulusan Ditolak'),
        ('05', 'Menunggu Kelulusan oleh Datuk Bandar'),

        ('06', 'Boleh dituntut'),
        ('07', 'Dalam tuntutan'),

        ('08', 'Semakan oleh Perbendaharaan'),
        ('09', 'Pindaan oleh Perbendaharaan'),
        ('10', 'Lulus - Dimasukkan Dalam Gaji'),

        ('NA', 'Not Available'),
    ]
    status = models.CharField(max_length=2, choices=STATUS, default='NA')

    pegawai_lulus = models.CharField(max_length=255, null=False)
    pegawai_lulus_catatan = models.TextField(null=True)
    pegawai_luluskan = models.BooleanField(default=False)

    pegawai_sah = models.CharField(max_length=255, null=False)
    pegawai_sah_catatan = models.TextField(null=True)
    pegawai_sahkan = models.BooleanField(default=False)

    hari =  models.DateField(null=True)
    waktu =  models.FloatField(null=True)
    kadar_jam =  models.FloatField(null=True)
    tujuan =  models.CharField(max_length=255, null=True)

    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id

class ElaunPerson(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nric = models.CharField(max_length=255, null=True)
    kod_pekerja = models.CharField(max_length=255, null=True)
    pemohon = models.BooleanField(default=True)
    
    elaun = models.ForeignKey(Elaun, on_delete=models.CASCADE, null=False)

    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id    


class ElaunTuntutan(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    nric = models.CharField(max_length=255, null=True)
    kod_pekerja = models.CharField(max_length=255, null=True)    
    elaun = models.ManyToManyField(Elaun, null=True)


    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id        
        