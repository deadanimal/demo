from django.urls import path, include

from .views import LolView


urlpatterns = [
    path('', LolView.as_view(), name='hsn'),
]