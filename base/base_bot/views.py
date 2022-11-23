from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
# Create your views here.

class CakeSerializator(serializers.ModelSerializer):
    class Meta:
        model = models.Cake
        fields = [
            'pk', 'cake_level', 'cake_form',
            'cake_topping', 'cake_berries', 'cake_dekor',
            'cake_inscription', 'cake_comment'
        ]


class GetCake(APIView):
    def get(self, *args, **kwargs):
        all_cakes = models.Cake.objects.all()
        cake = all_cakes[0]
        print(cake)
        serialized_cake = CakeSerializator(cake)

        return Response(serialized_cake.data)