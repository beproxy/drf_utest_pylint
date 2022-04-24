from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.core.models import AddressFrom, AddressTo, Order, Stuff


class AddressFromSerializer(ModelSerializer):
    class Meta:
        model = AddressFrom
        fields = "__all__"


class AddressToSerializer(ModelSerializer):
    class Meta:
        model = AddressTo
        fields = "__all__"


class StuffSerializer(ModelSerializer):
    class Meta:
        model = Stuff
        fields = "__all__"


class OrdersListSerializer(ModelSerializer):
    address_from = serializers.ReadOnlyField(source="address_from.city")
    address_to = serializers.ReadOnlyField(source="address_to.city")

    class Meta:
        model = Order
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    address_from = AddressFromSerializer()
    address_to = AddressToSerializer()
    stuff = StuffSerializer()

    class Meta:
        model = Order
        fields = "__all__"

    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.get(id=validated_data.pop("user").id)
        address_from = AddressFrom.objects.create(
            **validated_data.pop("address_from")
        )
        address_to = AddressTo.objects.create(
            **validated_data.pop("address_to")
        )
        stuff = Stuff.objects.create(**validated_data.pop("stuff"))
        instance = Order.objects.create(
            address_from=address_from,
            user=user,
            address_to=address_to,
            stuff=stuff,
            **validated_data
        )
        return instance
