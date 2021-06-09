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

    path('chatroom', WebhookView.as_view(), name='kpdnhep_eaduan_chatroom_list'),
    path('chatroom/<uuid:room>', WebhookView.as_view(), name='kpdnhep_eaduan_chatroom_detail'),
    path('laporan', WebhookView.as_view(), name='kpdnhep_eaduan_laporan_list'),
    path('laporan/<uuid:laporan>', WebhookView.as_view(), name='kpdnhep_eaduan_laporan_detail'),

    path('webhook', WebhookView.as_view(), name='kpdnhep_eaduan_webhook'),
      
]