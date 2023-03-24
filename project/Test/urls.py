from django.urls import path
from .views import AvailableRoomResponse

urlpatterns = [
    path('', AvailableRoomResponse, name = 'available-rooms' ),
]
