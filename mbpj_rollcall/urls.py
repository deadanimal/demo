from django.urls import path, include

from mbpj_rollcall.views.user import UserDashboardView

from mbpj_rollcall.views.user import UserDashboardView

urlpatterns = [
    path('', UserDashboardView.as_view(), name='mbpj_rollcall_user_dashboard'),

]