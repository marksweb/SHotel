from django.contrib import admin

from .models import Employee, Room, RoomType


admin.site.register(Employee)
admin.site.register(Room)
admin.site.register(RoomType)
