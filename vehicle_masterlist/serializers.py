from rest_framework import serializers
from .models import (
    VehicleMasterList
    )


class vehicleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = VehicleMasterList
        fields = (
            '__all__'
        )
        datatables_always_serialize = ('id')

class vehiclesold(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = VehicleMasterList
        fields = (
            '__all__'
        )
        datatables_always_serialize = ('vehicle_status')