from rest_framework import serializers
from .models import (
    shell_report
    )


class shell_report_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = shell_report
        fields = (
            '__all__'
        )
        datatables_always_serialize = ('id')
