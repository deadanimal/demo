from django.urls import path, include

from .views.user import *


urlpatterns = [
    # Web Authentication
    # path('login', LoginView.as_view(), name='demoapp_login'),
    # path('logout', LogoutView.as_view(), name='demoapp_logout'),
    
    # Common Path    
    path('', DashboardView.as_view(), name='kpdnhep_eaduan_dashboard'),
    path('login', LoginView.as_view(), name='kpdnhep_eaduan_login'),
    path('logout', LogoutView.as_view(), name='kpdnhep_eaduan_logout'),

    path('webhook', WebhookView.as_view(), name='kpdnhep_eaduan_webhook'),
      
]