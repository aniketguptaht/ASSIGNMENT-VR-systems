from django.db import models
from .choices import ROOM_TYPES
# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class RoomType(models.Model):
    name = models.CharField(max_length=200)
    type = models.PositiveIntegerField( choices=ROOM_TYPES, default=0)
    building = models.ForeignKey(Building,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    number = models.PositiveSmallIntegerField()
    roomtype = models.ForeignKey(RoomType,on_delete=models.CASCADE) 
    price = models.FloatField()

    def __str__(self) -> str:
        return 'Room Number ' + str(self.number)

class BlockedDay(models.Model):
    day = models.DateField()
    room = models.ForeignKey(Room,on_delete=models.CASCADE) 

    class Meta:
        ordering = ['day']
        
    def __str__(self) -> str:
        return 'Day :- ' + str(self.day) + ' Room :- ' + str(self.room)