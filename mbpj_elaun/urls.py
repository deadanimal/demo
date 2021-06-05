from django.urls import path, include

from mbpj_elaun.views.user import *


urlpatterns = [
    path('', UserDashboardView.as_view(), name='mbpj_elaun_dashboard'),

    path('mohon', UserMohonView.as_view(), name='mbpj_elaun_mohon'),
    path('lulus', UserLulusView.as_view(), name='mbpj_elaun_lulus'),
    path('sah', UserSahView.as_view(), name='mbpj_elaun_sah'),
    path('tuntut', UserTuntutView.as_view(), name='mbpj_elaun_tuntut'),
    path('kes-istimewa', UserKesIstimewaView.as_view(), name='mbpj_elaun_kes_istimewa'),

    path('periksa', UserPeriksaView.as_view(), name='mbpj_elaun_finance_periksa'),
    path('pindaan', UserPindaanView.as_view(), name='mbpj_elaun_finance_pindaan'),
    path('semakan', UserSemakanView.as_view(), name='mbpj_elaun_finance_semakan'),

    path('pengurusan', UserPengurusanView.as_view(), name='mbpj_elaun_sistem_pengurusan'),
    path('pendaftaran', UserPendaftaranView.as_view(), name='mbpj_elaun_sistem_pendaftaran'),
    path('maintenance', UserMaintenanceView.as_view(), name='mbpj_elaun_sistem_maintenance'),

    path('bantuan', UserBantuanView.as_view(), name='mbpj_elaun_bantuan'),
    path('laporan', UserLaporanView.as_view(), name='mbpj_elaun_laporan'),
    path('profil', UserProfilView.as_view(), name='mbpj_elaun_profil'),

    path('login', UserLoginView.as_view(), name='mbpj_elaun_login'),
    path('logout', UserLogoutView.as_view(), name='mbpj_elaun_logout'),

]