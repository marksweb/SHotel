from rest_framework import viewsets

from ..serializers import ReservationSerializer
from ..models import Reservation


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
