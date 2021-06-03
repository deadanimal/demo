from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now

from ..models.outbound import (
    GrnInterfaceInterface,
    GrnInterface2Interface,
    InventoryTransactionInterface,
    InventoryTransactionFromProjectInterface,
    InventoryTransactionFromMaintenanceInterface
)

class GrnInterfaceInterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrnInterfaceInterface
        fields = '__all__'
        read_only_fields = ['id']

class GrnInterface2InterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrnInterface2Interface
        fields = '__all__'
        read_only_fields = ['id']   

class InventoryTransactionInterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTransactionInterface
        fields = '__all__'
        read_only_fields = ['id']    

class InventoryTransactionFromProjectInterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTransactionFromProjectInterface
        fields = '__all__'
        read_only_fields = ['id']    

class InventoryTransactionFromMaintenanceInterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTransactionFromMaintenanceInterface
        fields = '__all__'
        read_only_fields = ['id']                                 