from django.urls import path
from drf_yasg import openapi
from drf_yasg.generators import SchemaGenerator
from drf_yasg.inspectors import SerializerInspector
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.loans.api.serializers import LoanRequestCreateSerializer


class CustomSerializerInspector(SerializerInspector):
    def process_serializer(self, serializer):
        #if isinstance(serializer, LoanRequestCreateSerializer):
        #    return self.get_request_serializer_fields(serializer)
        return super().process_serializer(serializer)

class CustomSchemaGenerator(SchemaGenerator):
    inspector_cls = CustomSerializerInspector

schema_view = get_schema_view(
    openapi.Info(
        title="Loans API",
        default_version="v1",
        description="API for Loans.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
