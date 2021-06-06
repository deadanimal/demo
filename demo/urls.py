from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('demoapp.urls')),

    # Demo
    path('jpj-osc/', include('jpj_osc.urls')),

    # Project
    path('airsel-inventory/', include('airsel_inventory.urls')),
    path('mbpj-elaun/', include('mbpj_elaun.urls')),
]
