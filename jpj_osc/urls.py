from django.urls import path, include

from jpj_osc.views.static import HomeView

from jpj_osc.views.admin import * 
from jpj_osc.views.corp_user import *
from jpj_osc.views.user import *
from jpj_osc.views.webhook import *

from jpj_osc.views.api import api_router


urlpatterns = [
    path('', HomeView.as_view(), name='jpj_osc_home'),

    path('admin/', AdminView.as_view(), name='jpj_osc_admin'),
    path('admin/lesen', AdminView.as_view(), name='jpj_osc_admin_lesen'),
    path('admin/geran', AdminView.as_view(), name='jpj_osc_admin_geran'),
    path('admin/semakan',AdminView.as_view(), name='jpj_osc_admin_semakan'),
    path('admin/plat',AdminView.as_view(), name='jpj_osc_admin_plat'),
    path('admin/bayaran', AdminView.as_view(), name='jpj_osc_admin_bayaran'),
    
    path('user/', UserDashboardView.as_view(), name='jpj_osc_user'),
    path('user/lesen', UserLesenView.as_view(), name='jpj_osc_user_lesen'),
    path('user/geran', UserGeranView.as_view(), name='jpj_osc_user_geran'),
    path('user/semakan', UserSemakanView.as_view(), name='jpj_osc_user_semakan'),
    path('user/plat', UserPlatView.as_view(), name='jpj_osc_user_plat'),
    path('user/bayaran', UserBayaranView.as_view(), name='jpj_osc_user_bayaran'),

    path('corp-user/', CorpUserView.as_view(), name='jpj_osc_corp_user'),
    path('corp-user/lesen', CorpUserView.as_view(), name='jpj_osc_corp_user_lesen'),
    path('corp-user/geran', CorpUserView.as_view(), name='jpj_osc_corp_user_geran'),
    path('corp-user/semakan', CorpUserLesenMemanduView.as_view(), name='jpj_osc_corp_user_semakan'),
    path('corp-user/plat', CorpUserLesenMemanduView.as_view(), name='jpj_osc_corp_user_plat'),
    path('corp-user/bayaran', CorpUserView.as_view(), name='jpj_osc_corp_user_bayaran'),    

    path('webhook-billplz', BillplzWebhookView.as_view(), name='jpj_osc_corp_user_bayaran'),    

    path('api/', include(api_router.urls)),
]