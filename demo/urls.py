from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    # Pipeline Related
    path('', include('demoapp.urls')),
    path('bootcamp/', include('bootcamp.urls')),
    path('piper/', include('piper.urls')),

    # Prototype
    path('jpj-osc/', include('jpj_osc.urls')),

    # Project
    path('airsel-inventory/', include('airsel_inventory.urls')),
    path('mbpj-elaun/', include('mbpj_elaun.urls')),
]
