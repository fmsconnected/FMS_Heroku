from rest_framework import serializers
from .models import (
    Fata_monitoring
    )


class monitoringSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Fata_monitoring
        fields = (
            '__all__'
        )
        datatables_always_serialize = ('id')