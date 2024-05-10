from django.contrib import admin
from django.urls import path, include
from .views import VendorViewSet, PurchaseOrderViewSet, HistoricalPerformanceViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"vendor", VendorViewSet)
router.register(r"PurchaseOrder", PurchaseOrderViewSet)
router.register(r"HistoricalPerformance", HistoricalPerformanceViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("api/vendors/", VendorViewSet.views, name="create_vendor"),
]
