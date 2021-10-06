from rest_framework import serializers
from .models import (
    fleet_card_driver
)


class fleet_driver_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = fleet_card_driver
        fields = (
            '__all__'
        )
        datatables_always_serialize = ('id')
