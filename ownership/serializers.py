from rest_framework import serializers
from .models import (
    Ownership
    )


class ownSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ownership
        fields = (
            '__all__'
        )
        datatables_always_serialize = ('id')