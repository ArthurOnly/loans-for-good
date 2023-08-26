from apps.common.global_drf_render import CustomRenderer
from apps.common.global_drf_viewsets_mixins import SerializerAndPrefetchMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets


class CustomModelViewSet(SerializerAndPrefetchMixin, viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()` and `list()` actions.
    """

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    renderer_classes = [CustomRenderer]


class CustomReadOnlyModelViewSet(SerializerAndPrefetchMixin, viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides default `list()` and `retrieve()` actions.
    """

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    renderer_classes = [CustomRenderer]
