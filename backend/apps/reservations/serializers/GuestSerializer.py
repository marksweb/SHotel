from rest_framework import serializers

from ..models import Guest


class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'
