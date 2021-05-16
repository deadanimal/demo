from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='accounts'),
    
    path('logout', views.LogoutView.as_view(), name='logout'),
]