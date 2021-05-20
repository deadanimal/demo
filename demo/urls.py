
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()

from accounts import views as account_views
router.register('accounts', account_views.APIAccountViewSet, basename='account')


urlpatterns = [

    path('', include('pages.urls')),

    path('api/', include(router.urls)),

    #path('admin/', admin.site.urls),
]
