from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Account(models.Model):
    
    ACCOUNT_TYPE = [
        ('NA', 'Not Available'),
        ('NA', 'Not Available'),

        ('NA', 'Not Available'),
    ]
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPE, default='NA')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name