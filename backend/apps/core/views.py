from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer, AdminRenderer
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import mixins
from apps.core.models import Order
from apps.core.serializers import OrderSerializer, OrdersListSerializer


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().select_related(
        "address_from", "address_to", "stuff"
    )
    renderer_classes = (AdminRenderer, BrowsableAPIRenderer, JSONRenderer)

    def get_serializer_class(self):
        if self.action == 'list':

            return OrdersListSerializer

        return OrderSerializer
