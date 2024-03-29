from rest_framework import serializers
from vehicle_masterlist.models import (
    VehicleMasterList,
    )


class RegistrationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = VehicleMasterList
        fields = (
            '__all__'
        )
        datatables_always_serialize = ('id')

