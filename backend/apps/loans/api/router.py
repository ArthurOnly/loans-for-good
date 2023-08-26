from rest_framework import routers

from apps.loans.api.views import LoanRequestViewset, QuestionViewSet

router = routers.SimpleRouter()

router.register(
    r"questions",
    QuestionViewSet,
    basename="questions",
)

router.register(
    r"loan-requests",
    LoanRequestViewset,
    basename="loan-requests",
)

urlpatterns = router.urls
