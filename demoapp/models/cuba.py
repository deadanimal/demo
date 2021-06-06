from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CubaAplikasi(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(default='NA')
    base_url = models.CharField(default='NA')
    keyword = models.CharField(default='NA')
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.nama

class Cubaan(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(default='NA')
    aplikasi = models.ForeignKey(CubaAplikasi, on_delete=models.CASCADE, null=False)

    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id


        
