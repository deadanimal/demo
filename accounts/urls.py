from django.urls import path

from . import views

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),

    path('main', views.MainView.as_view(), name='accounts'),
    
    path('login', views.LogoutView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),

    path('support', views.SupportView.as_view(), name='support'),
]