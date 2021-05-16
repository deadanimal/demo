
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()

from wallets import views as wallet_views
router.register('wallets', wallet_views.APIWalletViewSet, basename='wallet')


urlpatterns = [

    path('', include('pages.urls')),

    path('api/', include(router.urls)),
    
    path('accounts/', include('accounts.urls')),
    path('chains/', include('chains.urls')),
    path('deposits/', include('deposits.urls')),
    path('wallets/', include('wallets.urls')),

    #path('admin/', admin.site.urls),
]
