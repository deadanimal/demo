from django.urls import path, include

from airsel_inventory.views.static import HomeView

from airsel_inventory.views.admin import * 
from airsel_inventory.views.webhook import *

from airsel_inventory.views.api import api_router


urlpatterns = [
    path('', HomeView.as_view(), name='airsel_inventory_home'),

    path('api/', include(api_router.urls)),
]