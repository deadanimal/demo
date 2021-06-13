from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import Model
from django.db.models.fields import CharField


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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id        


class Aduan(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    whatsapp_id = models.CharField(max_length=255, default='NA')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id           


class Chatroom(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    whatsapp_id = models.CharField(max_length=255, default='NA')    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id   

class ChatroomMesej(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    body = models.TextField(default='NA')
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, null=False)
    pengguna = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id                           