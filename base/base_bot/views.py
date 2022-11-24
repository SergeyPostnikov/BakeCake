from rest_framework import serializers
from rest_framework import viewsets

from . import models
# Create your views here.

class CakeSerializator(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cake
        fields = (
            'pk', 'cake_level', 'cake_form',
            'cake_topping', 'cake_berries', 'cake_dekor',
            'cake_inscription', 'cake_comment', 'delivery_address',
            'delivery_date'
        )

        
class CakeViewSet(viewsets.ModelViewSet):
    queryset = models.Cake.objects.all()
    serializer_class = CakeSerializator