from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('pages/about', views.AboutView.as_view(), name='pages_about'),
    path('pages/aml', views.AmlView.as_view(), name='pages_aml'),
    path('pages/chain', views.ChainView.as_view(), name='pages_chain'),
    path('pages/developer', views.DeveloperView.as_view(), name='pages_developer'),
    path('pages/ecosystem', views.EcosystemView.as_view(), name='pages_ecosystem'),
    path('pages/privacy', views.PrivacyView.as_view(), name='pages_privacy'),
    path('pages/terms', views.TermsView.as_view(), name='pages_terms'),
]