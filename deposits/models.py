from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Deposit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    onramp = models.BooleanField(default=True)

    circle_wire_id = models.UUIDField(null=True)
    circle_account_number = models.CharField(max_length=255, null=True)
    circle_routing_number = models.CharField(max_length=255, null=True)
    circle_iban_number = models.CharField(max_length=255, null=True)

    user_id = models.UUIDField(editable=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
