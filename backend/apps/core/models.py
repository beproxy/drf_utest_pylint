from django.db import models
from django.contrib.auth.models import User


class AddressFrom(models.Model):
    city = models.CharField(max_length=64, null=True, blank=True)
    street = models.CharField(max_length=128, null=True, blank=True)
    house = models.CharField(max_length=8, null=True, blank=True)
    apartment = models.CharField(max_length=10, null=True, blank=True)
    floor = models.PositiveSmallIntegerField(default=1, null=True, blank=True)
    elevator = models.BooleanField(default=False, null=True)
    comment = models.TextField(max_length=250, null=True)


class AddressTo(models.Model):
    city = models.CharField(max_length=64, null=True, blank=True)
    street = models.CharField(max_length=128, null=True, blank=True)
    house = models.CharField(max_length=8, null=True, blank=True)
    apartment = models.CharField(max_length=10, null=True, blank=True)
    floor = models.PositiveSmallIntegerField(default=1, null=True, blank=True)
    elevator = models.BooleanField(default=False, null=True)
    comment = models.TextField(max_length=250, null=True)


class Stuff(models.Model):
    sofa = models.PositiveSmallIntegerField(default=0, null=True)
    bed = models.PositiveSmallIntegerField(default=0, null=True)
    table = models.PositiveSmallIntegerField(default=0, null=True)
    armchair = models.PositiveSmallIntegerField(default=0, null=True)
    chair = models.PositiveSmallIntegerField(default=0, null=True)
    cabinet = models.PositiveSmallIntegerField(default=0, null=True)
    # in cubic meters
    other_m3 = models.PositiveSmallIntegerField(default=0, null=True)
    # weight in pounds
    other_heavy_goods = models.PositiveSmallIntegerField(default=0, null=True)
    fragile = models.BooleanField(default=False, null=True)
    comment = models.TextField(max_length=250, null=True)


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    address_from = models.ForeignKey(
        AddressFrom, on_delete=models.CASCADE, null=True, blank=True
    )
    address_to = models.ForeignKey(
        AddressTo, on_delete=models.CASCADE, null=True, blank=True
    )
    mobile = models.CharField(max_length=14, null=True, blank=True)
    stuff = models.ForeignKey(
        Stuff, on_delete=models.CASCADE, null=True, blank=True
    )
    my_price = models.PositiveSmallIntegerField(null=True)
    movers = models.BooleanField(default=False, null=True)
    packers = models.BooleanField(default=False, null=True)
    all_inclusive = models.BooleanField(default=False, null=True)
    comment = models.TextField(max_length=250, null=True)
