from django.urls import path, include

from .views.user import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # Web Authentication
    # path('login', LoginView.as_view(), name='demoapp_login'),
    # path('logout', LogoutView.as_view(), name='demoapp_logout'),
    
    # Common Path    
    path('', DashboardView.as_view(), name='kpdnhep_eaduan_dashboard'),
    path('login', LoginView.as_view(), name='kpdnhep_eaduan_login'),
    path('logout', LogoutView.as_view(), name='kpdnhep_eaduan_logout'),

    path('bantuan/', BantuanListView.as_view(), name='kpdnhep_eaduan_bantuan_list'),
    path('bantuan/<uuid:bantuan_id>', BantuanDetailView.as_view(), name='kpdnhep_eaduan_bantuan_detail'),
    path('chatroom/', ChatroomListView.as_view(), name='kpdnhep_eaduan_chatroom_list'),
    path('chatroom/<uuid:chatroom_id>', ChatroomDetailView.as_view(), name='kpdnhep_eaduan_chatroom_detail'),
    path('laporan/', LaporanListView.as_view(), name='kpdnhep_eaduan_laporan_list'),
    path('laporan/<uuid:laporan_id>', LaporanDetailView.as_view(), name='kpdnhep_eaduan_laporan_detail'),

    path('webhook', csrf_exempt(WebhookView.as_view()), name='kpdnhep_eaduan_webhook'),
      
]