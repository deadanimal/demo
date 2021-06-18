from django.urls import path, include

from .views.user import *


urlpatterns = [
    # Web Authentication
    # path('login', LoginView.as_view(), name='demoapp_login'),
    # path('logout', LogoutView.as_view(), name='demoapp_logout'),
    
    # Common Path    
    path('', DashboardView.as_view(), name='piper_dashboard'),
    path('login', LoginView.as_view(), name='piper_login'),
    path('logout', LogoutView.as_view(), name='piper_logout'),

    path('checkins/', CheckinListView.as_view(), name='piper_checkin_list'),
    path('checkins/<int:checkin>', CheckinDetailView.as_view(), name='piper_checkin_detail'),    
    
    path('projeks/', ProjekListView.as_view(), name='piper_projek_list'),
    path('projeks/<int:projek>', ProjekDetailView.as_view(), name='piper_projek_detail'),

    path('kerjas/', KerjaListView.as_view(), name='piper_kerja_list'),
    path('kerjas/<int:kerja>', KerjaDetailView.as_view(), name='piper_kerja_detail'),    
]