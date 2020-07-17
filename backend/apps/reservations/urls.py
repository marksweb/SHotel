from rest_framework import routers

from .views import (GuestViewSet, ReservationViewSet)


router = routers.DefaultRouter()
router.register('guests', GuestViewSet)
router.register('reservations', ReservationViewSet)
