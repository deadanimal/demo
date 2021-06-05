from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Bantuan(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id

class BantuanMesej(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bantuan = models.ForeignKey(Bantuan, on_delete=models.CASCADE, null=False)

    tajuk = models.CharField(max_length=255, default='NA')
    catatan = models.TextField(default='NA')

    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id        