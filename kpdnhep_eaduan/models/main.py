from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import Model
from django.db.models.fields import CharField

from helpers.general import PathAndRename


class MesejWhatsapp(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message_sid = models.CharField(max_length=255, default='NA')
    account_sid = models.CharField(max_length=255, default='NA')
    profile_name = models.CharField(max_length=255, default='NA')
    body = models.TextField(default='NA')
    whatsapp_id = models.CharField(max_length=255, default='NA')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id



class Bantuan(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    JENIS = (
        ('A', 'Laporan Helpdesk'),
        ('B', 'Dokumen Pembangunan'),
    )

    jenis_bantuan = models.CharField(max_length=1, choices=JENIS, default='A')

    TOPIK = (
        ('A', 'Gangguan Sistem'),
        ('B', 'Pertanyaan'),
    )

    topik_bantuan = models.CharField(max_length=1, choices=TOPIK, default='A')    
    mesej = models.TextField(default='NA')

    dokumen = models.FileField(null=True, upload_to=PathAndRename('kpdnhep'))
    daripada_syarikat = models.BooleanField(default=False)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id      


class Laporan(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id            


class Aduan(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    whatsapp_id = models.CharField(max_length=255, default='NA')
    body = models.TextField(default='NA')    
    tugas = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id           


class Chatroom(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    whatsapp_id = models.CharField(max_length=255, default='NA', unique=True)  
    active = models.BooleanField(default=False)  

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id   

class ChatroomMesej(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    body = models.TextField(default='NA')
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, null=True)
    pengguna = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id                           