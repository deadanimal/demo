from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='accounts'),
    
    path('login', views.LogoutView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]