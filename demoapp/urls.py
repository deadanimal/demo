from django.urls import path, include

from .views.user import *


urlpatterns = [
    # Web Authentication
    # path('login', LoginView.as_view(), name='demoapp_login'),
    # path('logout', LogoutView.as_view(), name='demoapp_logout'),
    
    # Common Path    
    path('', HomeView.as_view(), name='demoapp_home'),
    path('admin', AdminView.as_view(), name='demoapp_admin'),
]