from django.contrib import admin
from .models import Building, RoomType, Room, BlockedDay
# Register your models here.

admin.site.register(Building)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(BlockedDay)
