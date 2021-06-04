from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Login(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nric = models.CharField(max_length=255, null=False)

    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.nric