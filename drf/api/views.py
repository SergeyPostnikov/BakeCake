from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from . import models


class CakeSerializator(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cake
        fields = [
            'pk', 'cake_level', 'cake_form',
            'cake_topping', 'cake_berries', 'cake_dekor',
            'cake_inscription'
        ]


class CakeViewSet(viewsets.ModelViewSet):
    queryset = models.Cake.objects.all()
    serializer_class = CakeSerializator


class UserSerializator(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = [
            'name', 'phone', 'email',
            'address', 'orders'
        ]


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializator


class OrderSerializator(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Order
        fields = [
            'cake', 'date', 'time',
            'delivcomments', 'cost'
        ]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = OrderSerializator