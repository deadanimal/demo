from django.urls import path, include

from mbpj_elaun.views.user import (
    UserDashboardView,
    UserLoginView,
    UserLogoutView
)


urlpatterns = [
    path('', UserDashboardView.as_view(), name='mbpj_elaun_dashboard'),
    
    path('login', UserLoginView.as_view(), name='mbpj_elaun_login'),
    path('logout', UserLogoutView.as_view(), name='mbpj_elaun_logout'),

]