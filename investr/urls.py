from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from customer.views import BrokerageAccountViewSet, StockViewSet, dashboard_view 

router = DefaultRouter()
router.register(r'stocks', StockViewSet, basename="stock")
router.register(r'accounts', BrokerageAccountViewSet, basename="brokerage-account") 

urlpatterns = [
    path("", dashboard_view, name='home'),
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api-auth/", include('rest_framework.urls')), 
]