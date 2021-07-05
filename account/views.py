
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
import datetime
from datetime import date, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response


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
    EmployeeMasterlist
)
from vehicle_masterlist.models import VehicleMasterList

from leasingmasterlist.models import (
    Leasing
    )
from CustomerLog.models import (
    CS_log
)
from corrective.models import (
    Corrective
    )
from CustomerLog.models import (
    CS_log
    )

def index(request):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    date = datetime.datetime.today()
    months = ['zero','January','February','March','April','May','June','July','August','September','October','November','December']
    month = months[date.month]
    # count1 = VehiclePayment.objects.filter(Date_initiated__month= date.month ).count()
    # count2 = CarRental.objects.filter(Date_initiated__month= date.month ).count()
    # count3 = Fuel_supplier.objects.filter(Date_initiated__month= date.month ).count()
    # count4 = Vehicle_Repair_payment.objects.filter(date_initiated__month= date.month ).count()
    # count5 = CarRentalRequest.objects.filter(Date_initiated__month= date.month ).count()
    # count6 = Gas_card.objects.filter(date_initiated__month= date.month ).count()
    # count7 = service_vehicle.objects.filter(date_initiated__month= date.month ).count()
    # count8 = Vehicle_Repair.objects.filter(date_initiated__month= date.month ).count()
    # count9 = vehicle_report.objects.filter(date_initiated__month= date.month ).count()
    # count10 = Fata_monitoring.objects.filter(Date_initiated__month= date.month ).count()
    # count11 = Ownership.objects.filter(date_initiated__month= date.month ).count()
    count11 = Corrective.objects.count()
    count12 = EmployeeMasterlist.objects.count()
    count13 = VehicleMasterList.objects.count()
    count14 = Billing.objects.count()
    count15 = Leasing.objects.count()
    count16 = CS_log.objects.filter(Ageing="").count()
    return render(request, 'account/index.html', {'title': 'FLEET', 'month':month, 'count11': count11,
                                                  'count12': count12, 'count13': count13, 'count14': count14, 'count15': count15, 'count16':count16})

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


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        date = datetime.datetime.today()
        em_count = EmployeeMasterlist.objects.all().count()
        vm_count = VehicleMasterList.objects.all().count()
        leasing_count = Leasing.objects.all().count()
        vpr = VehiclePayment.objects.filter(Date_initiated__month= date.month ).count()
        crp = CarRental.objects.filter(Date_initiated__month= date.month ).count()
        fs = Fuel_supplier.objects.filter(Date_initiated__month= date.month ).count()
        vrp = Vehicle_Repair_payment.objects.filter(date_initiated__month= date.month ).count()
        crr = CarRentalRequest.objects.filter(Date_initiated__month= date.month ).count()
        gcr = Gas_card.objects.filter(date_initiated__month= date.month ).count()
        svr = service_vehicle.objects.filter(date_initiated__month= date.month ).count()
        vrr = Vehicle_Repair.objects.filter(date_initiated__month= date.month ).count()
        vr = vehicle_report.objects.filter(date_initiated__month= date.month ).count()
        fm = Fata_monitoring.objects.filter(Date_initiated__month= date.month ).count()
        own = Ownership.objects.filter(date_initiated__month= date.month ).count()
        bill = Billing.objects.all().count()
        cor = Corrective.objects.all().count()
        cus = CS_log.objects.all().count()
        
        labels = ["Monitoring",
        "Corrective", "Customer Care", "Ownership", "Billing", "Car Rental Request", "Gas Card Request",
        "Leasing", "Vehicle Repair Request", "Insurance", "New Vehicle Payment", "Car Rental Payment"
        , "Fuel Supplier Payment", "Vehicle Repair Payment"]
        default_items = [fm,cor,cus, own, bill,crr,gcr,svr, vrr, vr,vpr,crp,fs,vrp]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

class ChartData_ongoing(APIView):
    authentication_classes = []
    permission_classes = []


    def get(self, request, format=None):
        date = datetime.datetime.today()
        vpr = VehiclePayment.objects.filter(Date_initiated__month= date.month, Date_initial="" ).count()
        crp = CarRental.objects.filter(Date_initiated__month= date.month, R_Cost="" ).count()
        fs = Fuel_supplier.objects.filter(Date_initiated__month= date.month, Payee="" ).count()
        vrp = Vehicle_Repair_payment.objects.filter(date_initiated__month= date.month, invoice_date="" ).count()
        crr = CarRentalRequest.objects.filter(Date_initiated__month= date.month, Plate_no="").count()
        gcr = Gas_card.objects.filter(date_initiated__month= date.month, fleet_date_release="" ).count()
        svr = service_vehicle.objects.filter(date_initiated__month= date.month, approved_by="" ).count()
        vrr = Vehicle_Repair.objects.filter(date_initiated__month= date.month,approvedby="" ).count()
        vr = vehicle_report.objects.filter(date_initiated__month= date.month, date_forwarded="" ).count()
        fm = Fata_monitoring.objects.filter(Date_initiated__month= date.month, Clearing_accountability="" ).count()
        own = Ownership.objects.filter(date_initiated__month= date.month, date_transfered_completed="" ).count()
        cor = Corrective.objects.filter(date_initiated__month= date.month, approvedby__isnull=True ).count()
        cus = CS_log.objects.filter(Date_received__month= date.month, Date_resolved_inital="" ).count()
        ongoing_labels = ["Monitoring",
        "Corrective","Customer Care", "Ownership", "Car Rental Request", "Gas Card Request",
        "Leasing", "Vehicle Repair Request", "Insurance", "New Vehicle Payment", "Car Rental Payment"
        , "Fuel Supplier Payment", "Vehicle Repair Payment"]
        item_data = [fm,cor,cus, own,crr,gcr,svr, vrr, vr,vpr,crp,fs,vrp]
        ongoing_data = {
                "ongoing_labels": ongoing_labels,
                "default_ongoing": item_data,
        }
        return Response(ongoing_data)

class ChartData_completed(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        date = datetime.datetime.today()
        vpr = VehiclePayment.objects.filter(Date_initiated__month= date.month ).count()
        crp = CarRental.objects.filter(Date_initiated__month= date.month ).count()
        fs = Fuel_supplier.objects.filter(Date_initiated__month= date.month ).count()
        vrp = Vehicle_Repair_payment.objects.filter(date_initiated__month= date.month ).count()
        crr = CarRentalRequest.objects.filter(Date_initiated__month= date.month ).count()
        gcr = Gas_card.objects.filter(date_initiated__month= date.month ).count()
        svr = service_vehicle.objects.filter(date_initiated__month= date.month ).count()
        vrr = Vehicle_Repair.objects.filter(date_initiated__month= date.month ).count()
        vr = vehicle_report.objects.filter(date_initiated__month= date.month ).count()
        fm = Fata_monitoring.objects.filter(Date_initiated__month= date.month ).count()
        own = Ownership.objects.filter(date_initiated__month= date.month ).count()
        bill = Billing.objects.all().count()
        cor = Corrective.objects.all().count()
        cus = CS_log.objects.filter(Date_received__month= date.month, Date_resolved_inital="" ).count()
        item_completed_data = [fm,cor,cus, own, bill,crr,gcr,svr, vrr, vr,vpr,crp,fs,vrp]
        completed_data = {
                "datacompleted": item_completed_data,
        }
        print('Completed Data',completed_data)
        return Response(completed_data)

class Vmasterlist(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        vm_count = VehicleMasterList.objects.all().count()
        em_count = EmployeeMasterlist.objects.all().count()
        leasing_count = Leasing.objects.all().count()
        labels = ["Vehicle Masterlist","Employee Masterlist","Leasing Masterlist"]
        default_items = [ vm_count,em_count,leasing_count]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)
class Emasterlist(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        em_count = EmployeeMasterlist.objects.all().count()
        labels = ["Employee Masterlist"]
        default_items = [em_count]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)
class Lmasterlist(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        leasing_count = Leasing.objects.all().count()
        labels = ["Leasing Masterlist"]
        default_items = [leasing_count]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


