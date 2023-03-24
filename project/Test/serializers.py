from rest_framework import serializers
from .models import *


class AvailableRoomsSerializer(serializers.ModelSerializer):
    room_number =  serializers.IntegerField(source =  'room.number')
    room_price = serializers.FloatField(source = 'room.price')

    class Meta:
        model = BlockedDay
        fields = ['room_number','room_price']