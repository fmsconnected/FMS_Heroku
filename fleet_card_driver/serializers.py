from rest_framework import serializers
from .models import (
    fleet_card_driver
)


class fleet_driver_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = fleet_card_driver
        fields = (
            # 'id','Activity_Id','STATUS','SOA_DATE','SOA_NO','AMOUNT','COST_CENTER','DTR_CUTOFF','REF_NO','REMARKS')
            '__all__'
            )
        datatables_always_serialize = ('id')
            
    # @staticmethod
    # def setup_eager_loading(queryset):
    #  	queryset = queryset.prefetch_related('id')

    #  	return queryset