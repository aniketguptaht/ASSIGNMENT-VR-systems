from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import AvailableRoomsSerializer
from .models import *
from rest_framework import status
from datetime import datetime
# Create your views here.


@api_view(['GET'])
def AvailableRoomResponse(request):
    building_name = request.GET.get('building','')
    try:
        building = Building.objects.get(name=building_name)
    except:
        return Response(data = {"message" : 'Please check the Building name '} , status = status.HTTP_404_NOT_FOUND)
    try:
        check_in = request.GET.get('check_in') 
        check_in = datetime.strptime(check_in,'%Y-%m-%d') if check_in else None
        check_out = request.GET.get('check_out')
        check_out = datetime.strptime(check_out,'%Y-%m-%d') if check_out  else None
        if check_in and check_out:
            blocked_day = BlockedDay.objects.filter(day__gte=check_in,day__lte=check_out,room__roomtype__building__name=building_name).order_by('room__price')
            serializer = AvailableRoomsSerializer(blocked_day, many=True)
            return Response(serializer.data)
        
        else:
            return Response(data = {"message" : 'Please check the Check in and check out date '} , status = status.HTTP_404_NOT_FOUND)
    except:
        return Response(data = {"message" : 'SOME ERROR OCCURRED '} , status = status.HTTP_404_NOT_FOUND)