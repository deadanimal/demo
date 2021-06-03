from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now

from ..models.inbound import (
    PurchaseOrderInterface,
    MaterialRequestInterface,
    ItemInterface
)

class PurchaseOrderInterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderInterface
        fields = '__all__'
        read_only_fields = ['id']

class MaterialRequestInterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRequestInterface
        fields = '__all__'
        read_only_fields = ['id']        

class ItemInterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInterface
        fields = '__all__'
        read_only_fields = ['id']          