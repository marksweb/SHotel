from rest_framework import serializers

from ..models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, validated_data):
        instance = Reservation(**validated_data)
        instance.clean()
        return validated_data
