from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now

from ..models.outbound import (
    Grn,
    InventoryTransaction,
    MrTransaction,
    MrTransactionChild
)

class GrnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grn
        fields = '__all__'
        read_only_fields = ['id']

class InventoryTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTransaction
        fields = '__all__'
        read_only_fields = ['id']   

class MrTransactionChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = MrTransactionChild
        fields = '__all__'
        read_only_fields = ['id']        

class MrTransactionSerializer(serializers.ModelSerializer):

    child_items = MrTransactionChildSerializer(read_only=True, many=True)

    class Meta:
        model = MrTransaction
        fields = '__all__'
        read_only_fields = ['id']   