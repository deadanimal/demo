from __future__ import unicode_literals
import uuid

from django.db import models
from django.contrib.gis.db import models as geomodels

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import Model
from django.db.models.fields import CharField

from helpers.general import PathAndRename


class Checkin(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    latitude = models.DecimalField(decimal_places=8, max_digits=13, null=True)
    longitude = models.DecimalField(decimal_places=8, max_digits=13, null=True)

    PURPOSE = [
        ('AW', 'Start Work'),
        ('EW', 'End Work'),

        ('AS', 'Start Site Meeting or Work'),
        ('ES', 'End Site Meeting or Work'),

        # Saturday, Sunday, Public Holiday...
        ('AO', 'Start Overtime'),
        ('EO', 'End Overtime'),

        ('NA', ''),
    ]

    purpose = models.CharField(max_length=2, choices=PURPOSE, default='NA')

    LOCATION = [
        ('HQ', 'HQ Office'),
        ('CY', 'Cyberjaya Office'),

        ('CL', 'Client Office'),
        ('HO', 'Home'),

        ('NA', ''),
    ]

    location = models.CharField(max_length=2, choices=LOCATION, default='NA')    

    point = geomodels.PointField(null=True)
    polygon = geomodels.PolygonField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id