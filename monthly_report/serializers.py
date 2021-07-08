from rest_framework import serializers
from .models import (
    Petron_report
    )


class petron_report_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Petron_report
        fields = (
            '__all__'
        )
        datatables_always_serialize = ('id')
