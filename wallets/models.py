from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
#from phonenumber_field.modelfields import PhoneNumberField


class Wallet(models.Model):
    
    ADDRESS_TYPE = [

        ('S8', 'SS58 & Substrate Wallet'),
        ('ET', 'Ethereum Wallet'),

        ('NA', 'Not Available'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nickname = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True, unique=True)
    address_type = models.CharField(max_length=2, choices=ADDRESS_TYPE, default='NA')

    user_id = models.UUIDField(editable=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.nickname    


class WalletTransaction(models.Model):    

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name            