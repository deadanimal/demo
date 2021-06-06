from django.urls import path, include

from .views.user import *
from .views.api import *


urlpatterns = [
    # Web Authentication
    path('login', UserLoginView.as_view(), name='mbpj_elaun_login'),
    path('logout', UserLogoutView.as_view(), name='mbpj_elaun_logout'),
    
    # Common Path    
    path('', UserDashboardView.as_view(), name='mbpj_elaun_dashboard'),
    path('bantuan', UserBantuanView.as_view(), name='mbpj_elaun_bantuan'),
    path('laporan', UserLaporanView.as_view(), name='mbpj_elaun_laporan'),
    path('profil', UserProfilView.as_view(), name='mbpj_elaun_profil'),    

    # Elaun
    path('mohon', UserMohonView.as_view(), name='mbpj_elaun_mohon'),
    path('lulus', UserLulusView.as_view(), name='mbpj_elaun_lulus'),
    path('sah', UserSahView.as_view(), name='mbpj_elaun_sah'),
    path('tuntut', UserTuntutView.as_view(), name='mbpj_elaun_tuntut'),

    # Finance
    path('periksa', UserPeriksaView.as_view(), name='mbpj_elaun_finance_periksa'),
    path('pindaan', UserPindaanView.as_view(), name='mbpj_elaun_finance_pindaan'),
    path('semakan', UserSemakanView.as_view(), name='mbpj_elaun_finance_semakan'),

    # Sistem
    path('pengurusan', UserPengurusanView.as_view(), name='mbpj_elaun_sistem_pengurusan'),
    path('pendaftaran', UserPendaftaranView.as_view(), name='mbpj_elaun_sistem_pendaftaran'),
    path('maintenance', UserMaintenanceView.as_view(), name='mbpj_elaun_sistem_maintenance'),

    # API
    path('api/token/', ApiTokenView.as_view(), name='mbpj_elaun_api_token'), # GET with Authorisation will get new token POST with username/password
    # path('api/elaun/', ApiTokenView.as_view(), name='mbpj_elaun_ll'),
    # path('api/finance/', ApiTokenView.as_view(), name='mbpj_elaun_ll'),
    # path('api/sistem/', ApiTokenView.as_view(), name='mbpj_elaun_ll'),
]