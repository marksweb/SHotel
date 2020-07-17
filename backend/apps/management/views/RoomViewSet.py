from rest_framework import viewsets

from ..serializers import RoomSerializer
from ..models import Room


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
