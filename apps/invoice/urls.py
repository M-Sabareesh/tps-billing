from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import InvoceViewSet, ItemViewSet

router = DefaultRouter()
router.register("invoices", InvoceViewSet, basename="invoices")
router.register("items", ItemViewSet, basename="items")

urlpatterns = [
    path('', include(router.urls))
]