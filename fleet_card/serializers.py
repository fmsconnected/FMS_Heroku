from rest_framework import serializers
from .models import (
    fleet_card
)


class fleet_card_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = fleet_card
        fields = (
            '__all__'
        )
        datatables_always_serialize = ('id')
