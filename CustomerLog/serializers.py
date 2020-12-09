from rest_framework import serializers
from .models import (
    CS_log
)


class CS_log_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CS_log
        fields = (
            '__all__'
        )
        datatables_always_serialize = ('id')
