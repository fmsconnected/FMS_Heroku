from rest_framework import serializers
from .models import (
    Registration,
    )


class RegistrationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Registration
        fields = (
            '__all__'
        )
        datatables_always_serialize = ('id')

