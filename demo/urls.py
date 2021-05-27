from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    
    path('', include('accounts.urls')),

    path('jpj-osc/', include('jpj_osc.urls')),
    path('hsn/', include('hsn_main.urls')),
]
