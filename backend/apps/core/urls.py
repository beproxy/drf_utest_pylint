from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.core.views import OrderViewSet

router = DefaultRouter()
router.register("order", OrderViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
