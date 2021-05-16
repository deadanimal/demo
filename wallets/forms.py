from django.forms import ModelForm
from .models import Wallet

class WalletForm(ModelForm):

    class Meta:
        model = Wallet
        fields = [
            'nickname',
            'address',
            'address_type'
        ]
        read_only_fields = ['id']
