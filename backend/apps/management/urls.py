from rest_framework import routers

from .views import (
    RoomViewSet, RoomTypeViewSet, EmployeeViewSet
)


router = routers.DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('roomtypes', RoomTypeViewSet)
router.register('employees', EmployeeViewSet)
