from django.urls import path, include

from .views.user import *


urlpatterns = [
    # Web Authentication
    # path('login', LoginView.as_view(), name='demoapp_login'),
    # path('logout', LogoutView.as_view(), name='demoapp_logout'),
    
    # Common Path    
    path('', HomeView.as_view(), name='bootcamp_home'),
    path('admin', AdminView.as_view(), name='bootcamp_admin'),
    
    path('developer-day/', DeveloperDayListView.as_view(), name='bootcamp_developer_day_list'),
    path('developer-day/<int:day>', DeveloperDayDetailView.as_view(), name='bootcamp_developer_day_detail'),
]