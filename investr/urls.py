"""
URL configuration for investr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customer.views import PortfolioViewSet, StockViewSet

router = DefaultRouter()
router.register(r'stocks', StockViewSet, basename="stock")
router.register(r'portfolio', PortfolioViewSet, basename="portfolio")
# You will add authentication endpoints later (djoser/DRF simplejwt)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),  # /api/v1/stocks/, /api/v1/portfolio/
    path("api-auth/", include('rest_framework.urls')), # DRF Login/Logout
    # Add user authorization path here 
]

