from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseNotFound

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


class UserSerializator(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            'cake', 'buyer_name', 'buyer_mail',
            'buyer_phone', 'buyer_date', 'buyer_discount',
        ]

        
class GetCake(APIView):
    def get(self, *args, **kwargs):
        all_cakes = models.Cake.objects.all()
        cake = all_cakes[0]
        serialized_cake = CakeSerializator(cake)

        return Response(serialized_cake.data)


class GetUser(APIView):
    def get(self, request, pk, format=None):
        user = models.User.objects.get(pk=pk)
        if not user:
            return HttpResponseNotFound
        
        serialized_user = UserSerializator(user)

        return Response(serialized_user.data)