from rest_framework import viewsets

from ..serializers import GuestSerializer
from ..models import Guest


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
