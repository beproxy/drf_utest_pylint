from django.urls import path
from rest_framework.permissions import IsAdminUser
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Test for Stackt",
        description="Test for Stackt",
        default_version="v1"
    ),
    public=True,
    permission_classes=(IsAdminUser,),
)

urlpatterns = [
    path("api/swagger(?P<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("api/swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]