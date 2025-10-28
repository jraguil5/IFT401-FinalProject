from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from customer.views import (
    BrokerageAccountViewSet, StockViewSet, OrderViewSet, TradeViewSet, 
    admin_dashboard_view, register_user, 
    portfolio_view, buy_stock_view, sell_stock_view, 
    deposit_cash_view, withdraw_cash_view, 
    admin_change_market_hours_view, admin_create_stock_view,
    role_based_redirect
)

router = DefaultRouter()
router.register(r'stocks', StockViewSet, basename="stock")
router.register(r'accounts', BrokerageAccountViewSet, basename="brokerage-account")
router.register(r'orders', OrderViewSet, basename="order")
router.register(r'trades', TradeViewSet, basename="trade")


urlpatterns = [
    path("", role_based_redirect, name='home'),
    path("admin/", admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sign_in/', auth_views.LoginView.as_view(template_name='customer/sign_in.html'), name='sign_in'),
    path('sign_out/', auth_views.LogoutView.as_view(next_page='/sign_in/'), name='sign_out'),
    path('sign_up/', register_user, name='register'),
    path("api/v1/", include(router.urls)),
    path("api-auth/", include('rest_framework.urls')),
    path('admin_dashboard/', admin_dashboard_view, name='admin_dashboard'), 
    path('portfolio/', portfolio_view, name='portfolio'),
    path('buy/', buy_stock_view, name='buy_stock'),       
    path('sell/', sell_stock_view, name='sell_stock'),
    path('deposit/', deposit_cash_view, name='deposit_cash'), 
    path('withdraw/', withdraw_cash_view, name='withdraw_cash'),
    path('admin/market_hours/', admin_change_market_hours_view, name='admin_change_market_hours'),
    path('admin/create_stock/', admin_create_stock_view, name='admin_create_stock'),
    path('role_router/', role_based_redirect, name='role_based_redirect'),
]