from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    
    path('', include('accounts.urls')),

    path('jpj-osc/', include('jpj_osc.urls')),
    path('airsel-inventory/', include('airsel_inventory.urls')),
    path('mbpj-elaun/', include('mbpj_elaun.urls')),
    path('mbpj-rollcall/', include('mbpj_rollcall.urls')),
]
