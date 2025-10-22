from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from customer.views import BrokerageAccountViewSet, StockViewSet, OrderViewSet, TradeViewSet, dashboard_view, register_user

router = DefaultRouter()
router.register(r'stocks', StockViewSet, basename="stock")
router.register(r'accounts', BrokerageAccountViewSet, basename="brokerage-account")
router.register(r'orders', OrderViewSet, basename="order")
router.register(r'trades', TradeViewSet, basename="trade")


urlpatterns = [
    path("", dashboard_view, name='home'),
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api-auth/", include('rest_framework.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='customer/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', register_user, name='register')
]