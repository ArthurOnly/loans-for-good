from rest_framework import permissions
from rest_framework.parsers import MultiPartParser

from apps.common.global_drf_viewsets import (
    CustomModelViewSet,
    CustomReadOnlyModelViewSet,
)
from apps.loans.api.serializers import (
    LoanRequestCreateSerializer,
    LoanRequestSerializer,
    QuestionSerializer,
)
from apps.loans.models import LoanRequest, Question


class QuestionViewSet(CustomReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filterset_fields = {
        "label": ["exact", "icontains"],
        "active": ["exact"],
    }
    search_fields = ["label"]
    qs_list_prefetch_fields = ["questionoption_set"]
    qs_prefetch_fields = qs_list_prefetch_fields


class LoanRequestViewset(CustomModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanRequestCreateSerializer
    queryset = LoanRequest.objects.all()
    parser_classes = [MultiPartParser]
    serializer_class = {
        "default": LoanRequestSerializer,
        "create": LoanRequestCreateSerializer,
    }
    qs_list_prefetch_fields = ["loanrequestquestionresponse_set"]
    qs_prefetch_fields = qs_list_prefetch_fields

    def get_parsers(self):
        # Swagger UI does not support nested multipart form data
        if getattr(self, "swagger_fake_view", False):
            return []
        return super().get_parsers()
