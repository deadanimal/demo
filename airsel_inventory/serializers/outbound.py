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
    AinventoryTransaction
)

class GrnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grn
        fields = '__all__'
        read_only_fields = ['id']

class AinventoryTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AinventoryTransaction
        fields = '__all__'
        read_only_fields = ['id']   
