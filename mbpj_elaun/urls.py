from django.urls import path, include

from mbpj_elaun.views.user import UserDashboardView


urlpatterns = [
    path('', UserDashboardView.as_view(), name='mbpj_elaun_user_dashboard'),

]