from apps.common.global_drf_viewsets import (CustomModelViewSet,
                                             CustomReadOnlyModelViewSet)
from apps.loans.api.serializers import (LoanRequestCreateSerializer,
                                        LoanRequestSerializer,
                                        QuestionSerializer)
from apps.loans.models import LoanRequest, Question
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser


class QuestionViewSet(CustomReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filterset_fields = {
        "label": ["exact", "icontains"],
        "active": ["exact"],
    }
    search_fields = ["label"]


class LoanRequestViewset(CustomModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanRequestCreateSerializer
    queryset = LoanRequest.objects.all()
    parser_classes = [MultiPartParser]
    serializer_class = {
        "default": LoanRequestSerializer,
        "create": LoanRequestCreateSerializer,
    }

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()




