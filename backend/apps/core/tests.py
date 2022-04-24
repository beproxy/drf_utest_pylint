from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import (
    force_authenticate, APIRequestFactory, APITestCase
)

from apps.core.models import Order
from apps.core.views import OrderViewSet


class OrderTestCase(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create(username="test_user", password="testPassword")
        self.data = {
            "address_from": {
                "city": "London",
                "street": "Baker",
                "house": "221",
                "apartment": "4",
                "floor": "2",
            },
            "address_to": {
                "city": "London",
                "street": "Lambeth",
                "house": "34",
                "apartment": "5",
                "floor": 3,
                "elevator": "true",
            },
            "stuff": {
                "sofa": 1,
                "bed": 1,
                "table": 1,
                "armchair": 1,
                "chair": 4,
                "cabinet": 2,
                "other_m3": 2,
                "fragile": "true",
            },
            "mobile": "4423446576768",
            "my_price": 100,
            "all_inclusive": "true",
            "user": 1
        }

    def test_order(self):
        factory = APIRequestFactory()
        view = OrderViewSet.as_view({"post": "create"})
        request = factory.post('/order/', self.data, format='json')
        force_authenticate(request, user=self.test_user)
        response = view(request)

        order = Order.objects.filter(user=self.test_user).values().first()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(order)

        view = OrderViewSet.as_view({"get": "list"})
        request = factory.get('/order/')
        force_authenticate(request, user=self.test_user)
        response = view(request)
        order["address_from"] = self.data.get("address_from").get("city") if order.pop("address_from_id") else ""
        order["address_to"] = self.data.get("address_to").get("city") if order.pop("address_to_id") else ""
        order["stuff"] = self.data.get("stuff").get("id") if order.pop("stuff_id") else ""
        order["user"] = self.test_user.id if order.pop("user_id") else ""
        order_keys = set(order.keys())
        order_values = set(order.values())
        order_list_keys = set(response.data[0].keys())
        order_list_values = set(response.data[0].values())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertFalse(order_keys - order_list_keys)
        self.assertFalse(order_values - order_list_values)
