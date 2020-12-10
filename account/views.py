from django.shortcuts import render
from payment.models import (
    CarRental, VehiclePayment,
    Fuel_supplier,
    Vehicle_Repair_payment
)
from request.models import (
    CarRentalRequest,
    Gas_card,
    service_vehicle,
    Vehicle_Repair,)
from report.models import (
    vehicle_report,
)
from monitoring.models import (
    Fata_monitoring,
)
from ownership.models import (
    Ownership,
    Billing
)
from masterlist.models import (
    EmployeeMasterlist,
    VehicleMasterList,
    Leasing
)

from CustomerLog.models import (
    CS_log
)


def index(request):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    count1 = VehiclePayment.objects.count()
    count2 = CarRental.objects.count()
    count3 = Fuel_supplier.objects.count()
    count4 = Vehicle_Repair_payment.objects.count()
    count5 = CarRentalRequest.objects.count()
    count6 = Gas_card.objects.count()
    count7 = service_vehicle.objects.count()
    count8 = Vehicle_Repair.objects.count()
    count9 = vehicle_report.objects.count()
    count10 = Fata_monitoring.objects.count()
    count11 = Ownership.objects.count()
    count12 = EmployeeMasterlist.objects.count()
    count13 = VehicleMasterList.objects.count()
    count14 = Billing.objects.count()
    count15 = Leasing.objects.count()
    return render(request, 'account/index.html', {'title': 'FLEET', 'count1': count1, 'count2': count2, 'count3': count3, 'count4': count4, 'count5': count5, 'count6': count6, 'count7': count7, 'count8': count8, 'count9': count9, 'count10': count10, 'count11': count11,
                                                  'count12': count12, 'count13': count13, 'count14': count14, 'count15': count15})

########### Customer care log alert ###########


def cclog_alert(request):
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)
    dl2 = CS_log.objects.filter(
        Date_received__date=datetime.datetime.today() + timedelta(days=2))
    dl1 = CS_log.objects.filter(
        Date_received__date=datetime.datetime.today() + timedelta(days=1))
    dl = CS_log.objects.filter(
        Date_received__date=datetime.datetime.today())

    ccAlert = dl1.aggregate(counted=Count('id'))['counted'] + dl2.aggregate(counted=Count('id'))['counted'] + dl.aggregate(counted=Count('id'))[
        'counted']
    print(ccAlert)
    return render(request, 'account/index.html', {'title': 'CC log alert - Alert', 'ccAlert': ccAlert})
