from rest_framework import viewsets

from ..serializers import RoomTypeSerializer
from ..models import RoomType


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
