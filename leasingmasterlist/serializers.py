from rest_framework import serializers
from .models import (
    Leasing
    )


class leasingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Leasing
        fields = (
            '__all__'
        )
        datatables_always_serialize = ('id')