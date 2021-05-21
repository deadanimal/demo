from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='jpj_osc_home'),

    path('admin/', views.AdminView.as_view(), name='jpj_osc_admin'),
    path('admin/lesen-memandu', views.AdminLesenMemanduView.as_view(), name='jpj_osc_admin_lesen_memandu'),
    path('admin/lesen-kenderaan-persendirian', views.AdminLesenKenderaanPersendirianView.as_view(), name='jpj_osc_admin_lesen_kenderaan_persendirian'),
    
    path('user/', views.UserView.as_view(), name='jpj_osc_user'),
    path('user/lesen-memandu', views.UserLesenMemanduView.as_view(), name='jpj_osc_user_lesen_memandu'),
    path('user/lesen-kenderaan-persendirian', views.UserLesenKenderaanPersendirianView.as_view(), name='jpj_osc_user_lesen_kenderaan_persendirian'),
    
]