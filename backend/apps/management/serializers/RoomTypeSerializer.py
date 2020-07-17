from rest_framework import serializers

from ..models import RoomType


class RoomTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'
