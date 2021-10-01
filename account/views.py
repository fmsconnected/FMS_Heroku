
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
import datetime
from datetime import date, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum

from django.shortcuts import render
from payment.models import (
    Fuel_supplier,
    Vehicle_Repair_payment
)
from new_vehicle_payment.models import (VehiclePayment)
from car_rental_payment.models import (CarRental)
from car_rental_request.models import (CarRentalRequest)
from service_request.models import (service_vehicle)
from request.models import (
    Gas_card,
    Vehicle_Repair,)
from report.models import (
    vehicle_report,
)
from monitoring.models import (
    Fata_monitoring,
)
from monthly_report.models import (
    Petron_report,
    Petron_pivot
)
from monthly_report_shell.models import (
    shell_report,
    shell_pivot
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
from registration.models import Registration

def index(request):
    current_user = request.user
    print("user",current_user.username)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    date = datetime.datetime.today()
    months = ['zero','January','February','March','April','May','June','July','August','September','October','November','December']
    month = months[date.month]
    month_supplier = months[date.month-1]
    reg_months = datetime.datetime.now().month
    count11 = Corrective.objects.count()
    count12 = EmployeeMasterlist.objects.count()
    count13 = VehicleMasterList.objects.filter(vehicle_status="Active").count()
    sold = VehicleMasterList.objects.filter(vehicle_status="Sold").count()
    count14 = Billing.objects.count()
    count15 = Leasing.objects.count()
    count16 = CS_log.objects.filter(Ageing="").count()
    not_registered = Registration.objects.filter(Plate_ending=reg_months,Date_registered="" ).count()
    registered = Registration.objects.exclude(Plate_ending=reg_months,Date_registered="" ).count()
    return render(request, 'account/index.html', {'title': 'FLEET', 'month':month, 'count11': count11,
                                                  'count12': count12, 'count13': count13, 'count14': count14, 'count15': count15, 
                                                  'count16':count16,'not_registered':not_registered,'registered':registered,
                                                  'month_supplier':month_supplier,'sold':sold})

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
        
        labels = ["FATA Monitoring",
        "Corrective Maintenance", "Customer Care", "Transfer Ownership", "TOO Billing", "Car Rental Request", "Gas Card Request","Service Vehicle Request",
        "Preventive Maintenance", "Insurance", "New Vehicle Payment", "Car Rental Payment"
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
        month = datetime.datetime.now().month
        print(month)
        fm = Fata_monitoring.objects.filter(Date_initiated__month= date.month, Clearing_accountability="" ).count()
        cor = Corrective.objects.filter(date_initiated__month= date.month, approvedby="" ).count()
        own = Ownership.objects.filter(date_initiated__month= date.month, date_transfered_completed="" ).count()
        # bill = Billing.objects.filter(date_initiated__month=date.month, cost_center="").count()
        crr = CarRentalRequest.objects.filter(Date_initiated__month= date.month, Plate_no="").count()
        gcr = Gas_card.objects.filter(date_initiated__month= date.month, fleet_date_release="" ).count()
        svr = service_vehicle.objects.filter(date_initiated__month= date.month, approved_by="" ).count()
        vrr = Vehicle_Repair.objects.filter(date_initiated__month= date.month,approvedby="" ).count()
        vr = vehicle_report.objects.filter(date_initiated__month= date.month, date_forwarded="" ).count()
        vpr = VehiclePayment.objects.filter(Date_initiated__month= date.month, Date_initial="" ).count()
        crp = CarRental.objects.filter(Date_initiated__month= date.month, R_Cost="" ).count()
        fs = Fuel_supplier.objects.filter(Date_initiated__month= date.month, Date_forwarded="" ).count()
        vrp = Vehicle_Repair_payment.objects.filter(date_initiated__month= date.month, invoice_date="" ).count()
        registration = VehicleMasterList.objects.filter(PLATE_ENDING=month, vehicle_status="Active",CR_NAME="GLOBE").count()
        
        ongoing_labels = ["FATA Monitoring",
        "Corrective Maintenance", "Transfer Ownership", "Car Rental Request", "Gas Card Request",
        "Service Vehicle Request", "Preventive Maintenance", "Insurance", "New Vehicle Payment",
        "Car Rental Payment", "Fuel Supplier Payment", "Vehicle Repair Payment"],
        item_data = [fm,cor, own,crr,gcr,svr, vrr, vr,vpr,crp,fs,vrp]
        ongoing_data = {
                "default_ongoing": item_data,
        }
        print('registration',item_data)

        return Response(ongoing_data)

class ChartData_completed(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        date = datetime.datetime.today()
        vpr = VehiclePayment.objects.exclude(Date_initiated__month= date.month, Date_initial="" ).exclude(Date_initial__exact='').count()
        crp = CarRental.objects.exclude(Date_initiated__month= date.month, R_Cost="" ).exclude(R_Cost__exact='').count()
        fs = Fuel_supplier.objects.exclude(Date_initiated__month= date.month, Date_forwarded="" ).exclude(Date_forwarded__exact='').count()
        vrp = Vehicle_Repair_payment.objects.exclude(date_initiated__month= date.month, invoice_date="" ).exclude(invoice_date__exact='').count()
        crr = CarRentalRequest.objects.exclude(Date_initiated__month= date.month, Plate_no="").exclude(Plate_no__exact='').count()
        gcr = Gas_card.objects.exclude(date_initiated__month= date.month, fleet_date_release="" ).exclude(fleet_date_release__exact='').count()
        svr = service_vehicle.objects.exclude(date_initiated__month= date.month, approved_by="" ).exclude(approved_by__exact='').count()
        vrr = Vehicle_Repair.objects.exclude(date_initiated__month= date.month,approvedby="" ).exclude(approvedby__exact='').count()
        vr = vehicle_report.objects.exclude(date_initiated__month= date.month, date_forwarded="" ).exclude(date_forwarded__exact='').count()
        fm = Fata_monitoring.objects.exclude(Date_initiated__month= date.month, Clearing_accountability="" ).exclude(Clearing_accountability__exact='').count()
        own = Ownership.objects.exclude(date_initiated__month= date.month, date_transfered_completed="" ).exclude(date_transfered_completed__exact='').count()
        cor = Corrective.objects.exclude(date_initiated__month= date.month, approvedby="" ).exclude(approvedby__exact='').count()
        cus = CS_log.objects.exclude(Date_received__month= date.month, Date_resolved="").exclude(Date_resolved__exact='').count()
        bill = Billing.objects.exclude(date_initiated__month=date.month, cost_center="").exclude(cost_center__exact='').count()
        item_completed_data = [fm,cor,cus, own, bill,crr,gcr,svr, vrr, vr,vpr,crp,fs,vrp]
        completed_data = {
                "datacompleted": item_completed_data,
        }
        
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

class monthly_report_jan_summary(APIView):
    date = datetime.datetime.today()
    authentication_classes = []
    permission_classes = []
    ## ProductAmount ####
    def get(self, request, format=None):
        date = datetime.datetime.today()
        BB14_B1 = Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B1").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        BB14_B10= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B10").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        BB14_B11= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B11").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        BB14_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B2").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        BB14_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B3").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        BB14_B4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B4").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        BB14_B5= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B5").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        BB14_B6= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B6").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        BB14_B7= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B7").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        BB14_B8= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B8").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        BB14_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-C").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        BB14_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-E").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG12_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG12-C").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG12_D= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG12-D").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_B1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B1").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B2").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B3").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_C1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C1").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_C2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C2").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_C3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C3").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_C4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C4").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_C5_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C5-C").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_D1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D1").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_D2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D2").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_D3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D3").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_E1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E1").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_E2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E2").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_E3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E3").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_F1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F1").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_F2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F2").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG2_F3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F3").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG3_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG3-A").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG4_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG4_B15= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B15").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG4_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B2").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG4_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-E").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG4_F= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-F").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG4_G= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-G").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG5_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-B").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG5_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-E").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG5_G= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-G").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG6_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-B").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG6_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-C").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG6_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-E").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG7_F= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG7-F").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CMG8_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG8-B").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        CRA6_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CRA6-A").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        FIN23_C1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C1").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        FIN23_C10= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C10").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        FIN23_C4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C4").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        FIN23_C9= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C9").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        FIN9_C0201= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN9-C0201").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        FIN9_C0301= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN9-C0301").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG02_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-B").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG02_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-C").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG02_D= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-D").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG02_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-E").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG02_G= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-G").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG02_H= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-H").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG02_I= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-I").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG02_K= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-K").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG02_L= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-L").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG04_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-B3").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG05_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-E").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG09_D= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-D").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GRTM_C503= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GRTM-C503").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        ISG18_C2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="ISG18-C2").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT11_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT11-E").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_C3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C3").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_C5= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C5").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_C6= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C6").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D01_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D01-A").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D08_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D08-C").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D1").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D2_02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-02").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D2_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-03").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D2_05= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-05").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D3_02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-02").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D3_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-03").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D3_04= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-04").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D3_06= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-06").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D4_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D4-03").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D5_02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D5-02").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D5_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D5-03").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D6= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D6").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D6_06= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D6-06").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D7_01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-01").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D7_02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-02").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_D7_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-03").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_E2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-E2").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_E3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-E3").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_F3A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3A").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_F3B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3B").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_F3D= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3D").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_F3E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3E").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_G2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-G2").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT2_G4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-G4").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT3_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-A").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT3_B5= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-B5").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT3_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-C").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT3_D2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D2").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT3_D3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D3").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT3_D4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D4").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT3_D5= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D5").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_A01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-A01").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_B02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-B02").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_B06= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-B06").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_C01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-C01").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_D01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D01").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_D02A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D02A").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_D02B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D02B").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_E03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-E03").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_E04= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-E04").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_F01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F01").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_F02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F02").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_F03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F03").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_G= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_G01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G01").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_G02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G02").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_G03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G03").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_H01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-H01").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_H03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-H03").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_I01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-I01").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_I03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-I03").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_J01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-J01").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        NTT5_J03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-J03").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        OP12_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="OP12-A").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        OP20_F1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="OP20-F1").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        SG02_O= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-O").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        SG02_P= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-P").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        SG02_Q= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-Q").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        SG02_R= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-R").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        SG02_U= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG02_F= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GRTM_C503= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        GEG04_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('ProductAmount'))['ProductAmount__sum']
        

        ## ProductAmount end ####
        

        ##Discount_Amount

        dis_BB14_B1 = Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B1").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_BB14_B10= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B10").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_BB14_B11= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B11").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_BB14_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B2").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_BB14_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B3").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_BB14_B4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B4").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_BB14_B5= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B5").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_BB14_B6= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B6").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_BB14_B7= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B7").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_BB14_B8= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B8").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_BB14_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-C").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_BB14_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-E").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG12_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG12-C").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG12_D= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG12-D").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_B1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B1").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B2").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B3").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_C1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C1").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_C2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C2").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_C3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C3").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_C4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C4").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_C5_C= Petron_report.objects.filter(StatementDate__year=date.year, 
           StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C5-C").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_D1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D1").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_D2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D2").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_D3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D3").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_E1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E1").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_E2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E2").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_E3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E3").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_F1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F1").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_F2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F2").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG2_F3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F3").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG3_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG3-A").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG4_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG4_B15= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B15").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG4_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B2").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG4_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-E").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG4_F= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-F").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG4_G= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-G").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG5_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-B").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG5_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-E").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG5_G= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-G").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG6_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-B").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG6_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-C").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG6_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-E").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG7_F= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG7-F").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CMG8_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG8-B").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_CRA6_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CRA6-A").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_FIN23_C1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C1").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_FIN23_C10= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C10").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_FIN23_C4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C4").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_FIN23_C9= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C9").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_FIN9_C0201= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN9-C0201").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_FIN9_C0301= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN9-C0301").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG02_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-B").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG02_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-C").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG02_D= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-D").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG02_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-E").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG02_G= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-G").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG02_H= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-H").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG02_I= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-I").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG02_K= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-K").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG02_L= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-L").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG04_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-B3").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG05_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-E").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG09_D= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-D").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GRTM_C503= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GRTM-C503").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_ISG18_C2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="ISG18-C2").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT11_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT11-E").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_C3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C3").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_C5= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C5").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_C6= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C6").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D01_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D01-A").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D08_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D08-C").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D1").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D2_02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-02").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D2_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-03").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D2_05= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-05").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D3_02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-02").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D3_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-03").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D3_04= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-04").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D3_06= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-06").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D4_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D4-03").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D5_02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D5-02").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D5_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D5-03").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D6= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D6").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D6_06= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D6-06").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D7_01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-01").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D7_02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-02").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_D7_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-03").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_E2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-E2").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_E3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-E3").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_F3A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3A").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_F3B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3B").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_F3D= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3D").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_F3E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3E").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_G2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-G2").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT2_G4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-G4").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT3_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-A").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT3_B5= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-B5").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT3_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-C").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT3_D2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D2").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT3_D3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D3").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT3_D4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D4").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT3_D5= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D5").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_A01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-A01").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_B02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-B02").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_B06= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-B06").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_C01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-C01").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_D01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D01").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_D02A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D02A").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_D02B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D02B").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_E03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-E03").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_E04= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-E04").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_F01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F01").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_F02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F02").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_F03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F03").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_G= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_G01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G01").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_G02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G02").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_G03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G03").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_H01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-H01").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_H03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-H03").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_I01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-I01").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_I03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-I03").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_J01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-J01").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_NTT5_J03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-J03").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_OP12_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="OP12-A").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_OP20_F1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="OP20-F1").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_SG02_O= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-O").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_SG02_P= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-P").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_SG02_Q= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-Q").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_SG02_R= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-R").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_SG02_U= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG02_F= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GRTM_C503= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        dis_GEG04_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('DiscountAmount'))['DiscountAmount__sum']
        
        ## Discount_Amount end ######

        ### Net Amount #####
        net_BB14_B1 = Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B1").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_BB14_B10= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B10").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_BB14_B11= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B11").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_BB14_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B2").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_BB14_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B3").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_BB14_B4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B4").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_BB14_B5= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B5").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_BB14_B6= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B6").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_BB14_B7= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B7").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_BB14_B8= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B8").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_BB14_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-C").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_BB14_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-E").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG12_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG12-C").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG12_D= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG12-D").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_B1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B1").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B2").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B3").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_C1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C1").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_C2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C2").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_C3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C3").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_C4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C4").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_C5_C= Petron_report.objects.filter(StatementDate__year=date.year, 
           StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C5-C").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_D1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D1").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_D2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D2").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_D3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D3").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_E1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E1").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_E2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E2").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_E3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E3").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_F1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F1").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_F2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F2").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG2_F3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F3").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG3_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG3-A").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG4_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG4_B15= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B15").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG4_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B2").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG4_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-E").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG4_F= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-F").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG4_G= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-G").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG5_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-B").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG5_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-E").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG5_G= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-G").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG6_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-B").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG6_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-C").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG6_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-E").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG7_F= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG7-F").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CMG8_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG8-B").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_CRA6_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CRA6-A").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_FIN23_C1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C1").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_FIN23_C10= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C10").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_FIN23_C4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C4").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_FIN23_C9= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C9").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_FIN9_C0201= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN9-C0201").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_FIN9_C0301= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN9-C0301").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG02_B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-B").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG02_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-C").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG02_D= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-D").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG02_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-E").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG02_G= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-G").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG02_H= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-H").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG02_I= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-I").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG02_K= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-K").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG02_L= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-L").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG04_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-B3").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG05_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-E").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG09_D= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-D").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GRTM_C503= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GRTM-C503").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_ISG18_C2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="ISG18-C2").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT11_E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT11-E").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_C3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C3").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_C5= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C5").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_C6= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C6").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D01_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D01-A").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D08_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D08-C").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D1").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D2_02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-02").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D2_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-03").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D2_05= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-05").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D3_02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-02").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D3_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-03").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D3_04= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-04").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D3_06= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-06").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D4_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D4-03").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D5_02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D5-02").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D5_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D5-03").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D6= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D6").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D6_06= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D6-06").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D7_01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-01").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D7_02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-02").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_D7_03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-03").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_E2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-E2").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_E3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-E3").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_F3A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3A").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_F3B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3B").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_F3D= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3D").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_F3E= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3E").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_G2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-G2").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT2_G4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-G4").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT3_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-A").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT3_B5= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-B5").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT3_C= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-C").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT3_D2= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D2").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT3_D3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D3").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT3_D4= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D4").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT3_D5= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D5").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_A01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-A01").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_B02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-B02").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_B06= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-B06").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_C01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-C01").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_D01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D01").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_D02A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D02A").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_D02B= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D02B").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_E03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-E03").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_E04= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-E04").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_F01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F01").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_F02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F02").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_F03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F03").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_G= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_G01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G01").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_G02= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G02").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_G03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G03").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_H01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-H01").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_H03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-H03").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_I01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-I01").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_I03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-I03").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_J01= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-J01").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_NTT5_J03= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-J03").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_OP12_A= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="OP12-A").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_OP20_F1= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="OP20-F1").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_SG02_O= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-O").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_SG02_P= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-P").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_SG02_Q= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-Q").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_SG02_R= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-R").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_SG02_U= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG02_F= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GRTM_C503= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('NetAmount'))['NetAmount__sum']
        net_GEG04_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
            StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('NetAmount'))['NetAmount__sum']

        ### Net Amount End#####
        # petron_data = [
        #     BB14_B1,BB14_B10,BB14_B11,BB14_B2,BB14_B3,BB14_B4,BB14_B5,BB14_B6,BB14_B7,BB14_B8
        # ]
        # petron_data_dis = [
        #     dis_BB14_B1 ,dis_BB14_B10, dis_BB14_B11, dis_BB14_B2,dis_BB14_B3,dis_BB14_B4,dis_BB14_B5,dis_BB14_B6,dis_BB14_B7,dis_BB14_B8
        #     ]
        # petron_data_net = [
        #     net_BB14_B1 ,  net_BB14_B10,   net_BB14_B11,   net_BB14_B2,  net_BB14_B3,  net_BB14_B4,  net_BB14_B5,  net_BB14_B6,  net_BB14_B7,  net_BB14_B8 
        # ]

        NTT5_F01 = Petron_pivot.objects.exclude(ChargingDepartment="NTT5-F01",sum_product_amount__isnull=True).values()
        FIN23_C6 = Petron_pivot.objects.exclude(ChargingDepartment="FIN23-C6",sum_product_amount__isnull=True).values()
        NTT5_H01 = Petron_pivot.objects.exclude(ChargingDepartment="NTT5-H01",sum_product_amount__isnull=True).values()
        NTT5_J01 = Petron_pivot.objects.exclude(ChargingDepartment="NTT5-J01",sum_product_amount__isnull=True).values()
        FIN23_C9 = Petron_pivot.objects.exclude(ChargingDepartment="FIN23-C9",sum_product_amount__isnull=True).values()
        NTT5_G01 = Petron_pivot.objects.exclude(ChargingDepartment="NTT5-G01",sum_product_amount__isnull=True).values()
        SG02_P = Petron_pivot.objects.exclude(ChargingDepartment="SG02-P",sum_product_amount__isnull=True).values()
        CMG2_D3 = Petron_pivot.objects.exclude(ChargingDepartment="CMG2-D3",sum_product_amount__isnull=True).values()
        CMG2_B2 = Petron_pivot.objects.exclude(ChargingDepartment="CMG2-B2",sum_product_amount__isnull=True).values()
        CMG5_G = Petron_pivot.objects.exclude(ChargingDepartment="CMG5-G",sum_product_amount__isnull=True).values()

        dis_NTT5_F01 = Petron_pivot.objects.exclude(ChargingDepartment="NTT5-F01",sum_disc_amount__isnull=True).values()
        dis_FIN23_C6 = Petron_pivot.objects.exclude(ChargingDepartment="FIN23-C6",sum_disc_amount__isnull=True).values()
        dis_NTT5_H01 = Petron_pivot.objects.exclude(ChargingDepartment="NTT5-H01",sum_disc_amount__isnull=True).values()
        dis_NTT5_J01 = Petron_pivot.objects.exclude(ChargingDepartment="NTT5-J01",sum_disc_amount__isnull=True).values()
        dis_FIN23_C9 = Petron_pivot.objects.exclude(ChargingDepartment="FIN23-C9",sum_disc_amount__isnull=True).values()
        dis_NTT5_G01 = Petron_pivot.objects.exclude(ChargingDepartment="NTT5-G01",sum_disc_amount__isnull=True).values()
        dis_SG02_P = Petron_pivot.objects.exclude(ChargingDepartment="SG02-P",sum_disc_amount__isnull=True).values()
        dis_CMG2_D3 = Petron_pivot.objects.exclude(ChargingDepartment="CMG2-D3",sum_disc_amount__isnull=True).values()
        dis_CMG2_B2 = Petron_pivot.objects.exclude(ChargingDepartment="CMG2-B2",sum_disc_amount__isnull=True).values()
        dis_CMG5_G = Petron_pivot.objects.exclude(ChargingDepartment="CMG5-G",sum_disc_amount__isnull=True).values()

        net_NTT5_F01 = Petron_pivot.objects.exclude(ChargingDepartment="NTT5-F01",sum_net_amount__isnull=True).values()
        net_FIN23_C6 = Petron_pivot.objects.exclude(ChargingDepartment="FIN23-C6",sum_net_amount__isnull=True).values()
        net_NTT5_H01 = Petron_pivot.objects.exclude(ChargingDepartment="NTT5-H01",sum_net_amount__isnull=True).values()
        net_NTT5_J01 = Petron_pivot.objects.exclude(ChargingDepartment="NTT5-J01",sum_net_amount__isnull=True).values()
        net_FIN23_C9 = Petron_pivot.objects.exclude(ChargingDepartment="FIN23-C9",sum_net_amount__isnull=True).values()
        net_NTT5_G01 = Petron_pivot.objects.exclude(ChargingDepartment="NTT5-G01",sum_net_amount__isnull=True).values()
        net_SG02_P = Petron_pivot.objects.exclude(ChargingDepartment="SG02-P",sum_net_amount__isnull=True).values()
        net_CMG2_D3 = Petron_pivot.objects.exclude(ChargingDepartment="CMG2-D3",sum_net_amount__isnull=True).values()
        net_CMG2_B2 = Petron_pivot.objects.exclude(ChargingDepartment="CMG2-B2",sum_net_amount__isnull=True).values()
        net_CMG5_G = Petron_pivot.objects.exclude(ChargingDepartment="CMG5-G",sum_net_amount__isnull=True).values()

        petron_data = [
        NTT5_F01 ,FIN23_C6,NTT5_H01 ,NTT5_J01 ,FIN23_C9 ,NTT5_G01 ,SG02_P ,CMG2_D3 ,CMG2_B2,CMG5_G

        ]
        petron_data_dis = [
            dis_NTT5_F01 ,dis_FIN23_C6,dis_NTT5_H01 ,dis_NTT5_J01 ,dis_FIN23_C9 ,dis_NTT5_G01 ,dis_SG02_P ,dis_CMG2_D3 ,dis_CMG2_B2,dis_CMG5_G
            ]
        petron_data_net = [
            net_NTT5_F01 ,net_FIN23_C6,net_NTT5_H01 ,net_NTT5_J01 ,net_FIN23_C9 ,net_NTT5_G01 ,net_SG02_P ,net_CMG2_D3 ,net_CMG2_B2,net_CMG5_G
        ]

        # petron_data = [
        # BB14_B1,BB14_B10,BB14_B11,BB14_B2,BB14_B3,BB14_B4,BB14_B5,BB14_B6,BB14_B7,BB14_B8,BB14_C,BB14_E,CMG12_C,CMG12_D,CMG2_B1,
        # CMG2_B2,CMG2_B3,CMG2_C1,CMG2_C2,CMG2_C3,CMG2_C4,CMG2_C5_C,CMG2_D1,CMG2_D2,CMG2_D3,CMG2_E1,CMG2_E2,CMG2_E3,CMG2_F1,CMG2_F2,
        # CMG2_F3,CMG3_A,CMG4_B,CMG4_B15,CMG4_B2,CMG4_E,CMG4_F,CMG4_G,CMG5_B,CMG5_E,CMG5_G,CMG6_B,CMG6_C,CMG6_E,CMG7_F,CMG8_B,CRA6_A,
        # FIN23_C1,FIN23_C10,FIN23_C4,FIN23_C9,FIN9_C0201,FIN9_C0301,GEG02_B,GEG02_C,GEG02_D,GEG02_E,GEG02_G,GEG02_H,GEG02_I,GEG02_K,
        # GEG02_L,GEG04_B3,GEG05_E,GEG09_D,GRTM_C503,ISG18_C2,NTT11_E,NTT2_C3,NTT2_C5,NTT2_C6,NTT2_D01_A,NTT2_D08_C,NTT2_D1,
        # NTT2_D2_02,NTT2_D2_03,NTT2_D2_05,NTT2_D3_02,NTT2_D3_03,NTT2_D3_04,NTT2_D3_06,NTT2_D4_03,NTT2_D5_02,NTT2_D5_03,NTT2_D6,
        # NTT2_D6_06,NTT2_D7_01,NTT2_D7_02,NTT2_D7_03,NTT2_E2,NTT2_E3,NTT2_F3A,NTT2_F3B,NTT2_F3D,NTT2_F3E,NTT2_G2,
        # NTT2_G4,NTT3_A,NTT3_B5,NTT3_C,NTT3_D2,NTT3_D3,NTT3_D4,NTT3_D5,NTT5_A01,NTT5_B02,NTT5_B06,NTT5_C01,NTT5_D01,NTT5_D02A,
        # NTT5_D02B,NTT5_E03,NTT5_E04,NTT5_F01,NTT5_F02,NTT5_F03,NTT5_G,NTT5_G01,NTT5_G02,NTT5_G03,NTT5_H01,NTT5_H03,NTT5_I01,NTT5_I03,
        # NTT5_J01,NTT5_J03,OP12_A,OP20_F1,SG02_O,SG02_P,SG02_Q,SG02_R,SG02_U,GEG02_F,GRTM_C503,GEG04_B3,
        
        # dis_BB14_B1 ,dis_BB14_B10, dis_BB14_B11, dis_BB14_B2,dis_BB14_B3,dis_BB14_B4,dis_BB14_B5,dis_BB14_B6,dis_BB14_B7,dis_BB14_B8,dis_BB14_C,
        # dis_BB14_E,  dis_CMG12_C,dis_CMG12_D,dis_CMG2_B1,dis_CMG2_B2,dis_CMG2_B3,dis_CMG2_C1,dis_CMG2_C2,dis_CMG2_C3,dis_CMG2_C4,dis_CMG2_C5_C,
        # dis_CMG2_D1,dis_CMG2_D2,dis_CMG2_D3,dis_CMG2_E1,dis_CMG2_E2,dis_CMG2_E3,dis_CMG2_F1,dis_CMG2_F2,dis_CMG2_F3,dis_CMG3_A,  dis_CMG4_B,
        # dis_CMG4_B15, dis_CMG4_B2,dis_CMG4_E,  dis_CMG4_F,  dis_CMG4_G,  dis_CMG5_B,  dis_CMG5_E,  dis_CMG5_G,  dis_CMG6_B,  dis_CMG6_C,  dis_CMG6_E, 
        # dis_CMG7_F,  dis_CMG8_B,  dis_CRA6_A,  dis_FIN23_C1, dis_FIN23_C10,  dis_FIN23_C4, dis_FIN23_C9, dis_FIN9_C0201, 
        # dis_FIN9_C0301, dis_GEG02_B,dis_GEG02_C,dis_GEG02_D,dis_GEG02_E,dis_GEG02_G,dis_GEG02_H,dis_GEG02_I,dis_GEG02_K,dis_GEG02_L,dis_GEG04_B3, 
        # dis_GEG05_E,dis_GEG09_D,dis_GRTM_C503,  dis_ISG18_C2, dis_NTT11_E,dis_NTT2_C3,dis_NTT2_C5,dis_NTT2_C6,dis_NTT2_D01_A, 
        # dis_NTT2_D08_C, dis_NTT2_D1,dis_NTT2_D2_02, dis_NTT2_D2_03, dis_NTT2_D2_05, dis_NTT2_D3_02, dis_NTT2_D3_03, dis_NTT2_D3_04, dis_NTT2_D3_06,
        # dis_NTT2_D4_03, dis_NTT2_D5_02, dis_NTT2_D5_03, dis_NTT2_D6,dis_NTT2_D6_06, 
        # dis_NTT2_D7_01, dis_NTT2_D7_02, dis_NTT2_D7_03, dis_NTT2_E2,dis_NTT2_E3,dis_NTT2_F3A, dis_NTT2_F3B, dis_NTT2_F3D, dis_NTT2_F3E, 
        # dis_NTT2_G2,dis_NTT2_G4,dis_NTT3_A,  dis_NTT3_B5,dis_NTT3_C,  dis_NTT3_D2,dis_NTT3_D3,dis_NTT3_D4,dis_NTT3_D5,dis_NTT5_A01, dis_NTT5_B02, 
        # dis_NTT5_B06, dis_NTT5_C01, dis_NTT5_D01, dis_NTT5_D02A,  dis_NTT5_D02B,  dis_NTT5_E03, dis_NTT5_E04, dis_NTT5_F01, dis_NTT5_F02, dis_NTT5_F03, 
        # dis_NTT5_G,  dis_NTT5_G01, dis_NTT5_G02, dis_NTT5_G03, dis_NTT5_H01, dis_NTT5_H03, dis_NTT5_I01, dis_NTT5_I03, dis_NTT5_J01, dis_NTT5_J03, 
        # dis_OP12_A,  dis_OP20_F1,dis_SG02_O,  dis_SG02_P,  dis_SG02_Q,  dis_SG02_R,  dis_SG02_U,  dis_GEG02_F,  dis_GRTM_C503,  dis_GEG04_B3,  

        # net_BB14_B1 ,  net_BB14_B10,   net_BB14_B11,   net_BB14_B2,  net_BB14_B3,  net_BB14_B4,  net_BB14_B5,  net_BB14_B6,  net_BB14_B7,  net_BB14_B8,  
        # net_BB14_C, net_BB14_E, net_CMG12_C,  net_CMG12_D,  net_CMG2_B1,  net_CMG2_B2,  net_CMG2_B3,  net_CMG2_C1,  net_CMG2_C2,  net_CMG2_C3,  net_CMG2_C4,  
        # net_CMG2_C5_C,net_CMG2_D1,  net_CMG2_D2,  net_CMG2_D3,  net_CMG2_E1,  net_CMG2_E2,  net_CMG2_E3,  net_CMG2_F1,  net_CMG2_F2,  net_CMG2_F3,  net_CMG3_A, net_CMG4_B,
        # net_CMG4_B15,   net_CMG4_B2,  net_CMG4_E, net_CMG4_F, net_CMG4_G, net_CMG5_B, net_CMG5_E, net_CMG5_G, net_CMG6_B, net_CMG6_C, net_CMG6_E, net_CMG7_F,
        # net_CMG8_B, net_CRA6_A, net_FIN23_C1,   net_FIN23_C10,    net_FIN23_C4,   net_FIN23_C9,   net_FIN9_C0201,net_FIN9_C0301,
        # net_GEG02_B,  net_GEG02_C,  net_GEG02_D,  net_GEG02_E,  net_GEG02_G,  net_GEG02_H,  net_GEG02_I,  net_GEG02_K,  net_GEG02_L,  net_GEG04_B3,   net_GEG05_E,  
        # net_GEG09_D,  net_GRTM_C503,    net_ISG18_C2,   net_NTT11_E,  net_NTT2_C3,  net_NTT2_C5,  net_NTT2_C6,  net_NTT2_D01_A,
        # net_NTT2_D08_C,net_NTT2_D1,  net_NTT2_D2_02,net_NTT2_D2_03,net_NTT2_D2_05,net_NTT2_D3_02,net_NTT2_D3_03,net_NTT2_D3_04,net_NTT2_D3_06,net_NTT2_D4_03,
        # net_NTT2_D5_02,net_NTT2_D5_03,net_NTT2_D6,  net_NTT2_D6_06,net_NTT2_D7_01,net_NTT2_D7_02,net_NTT2_D7_03,net_NTT2_E2,  net_NTT2_E3,  net_NTT2_F3A,   
        # net_NTT2_F3B,   net_NTT2_F3D,   net_NTT2_F3E,   net_NTT2_G2,  net_NTT2_G4,  net_NTT3_A, net_NTT3_B5,  net_NTT3_C, net_NTT3_D2,  net_NTT3_D3,  net_NTT3_D4,  
        # net_NTT3_D5,  net_NTT5_A01,   net_NTT5_B02,   net_NTT5_B06,   net_NTT5_C01,   net_NTT5_D01,   net_NTT5_D02A,    net_NTT5_D02B,    net_NTT5_E03,   
        # net_NTT5_E04,   net_NTT5_F01,   net_NTT5_F02,   net_NTT5_F03,   net_NTT5_G, net_NTT5_G01,   net_NTT5_G02,   net_NTT5_G03,   net_NTT5_H01,   net_NTT5_H03,   
        # net_NTT5_I01,   net_NTT5_I03,   net_NTT5_J01,   net_NTT5_J03,   net_OP12_A, net_OP20_F1,  net_SG02_O, net_SG02_P, net_SG02_Q, net_SG02_R, net_SG02_U, 
        # net_GEG02_F, net_GRTM_C503, net_GEG04_B3, ]
        dept_label =["Department 1","Department 2", "Department 3", "Department 4"]
        petron_report_data = {
                    "petron_data_item": petron_data,
                    "dept_label":dept_label,
                    "petron_data_dis":petron_data_dis,
                    "petron_data_net":petron_data_net,
            }
        # print(petron_data)
        return Response(petron_report_data)

# class monthly_report_shell_summary(APIView):
#     date = datetime.datetime.today()
#     authentication_classes = []
#     permission_classes = []
#     ## ProductAmount ####
#     def get(self, request, format=None):
#         date = datetime.datetime.today()

#         BB14_B10 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B10").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         BB14_B2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B2").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         BB14_B3 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B3").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         BB14_B4 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B4").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         BB14_B5 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B5").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         BB14_B6 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B6").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         BB14_B7 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B7").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         BB14_B8 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B8").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         BB14_E = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-E").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMB4_B = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMB4-B").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG12_D = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG12-D").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_B1 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-B1").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_B3 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-B3").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_C1 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C1").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_C2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C2").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_C3 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C3").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_C4 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C4").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_C5_B = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C5-B").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_C5_C = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C5-C").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_C5_G = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C5-G").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum'] 
#         CMG2_D1 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-D1").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_D2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-D2").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_D3 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-D3").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_E2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-E2").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_E3 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-E3").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_F1  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-F1").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']  
#         CMG2_F2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-F2").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG2_F3  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-F3").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']  
#         CMG3_A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG3-A").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG4_B = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG4-B").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG4_C = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG4-C").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG4_D = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG4-D").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG4_E = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG4-E").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG4_F = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG4-F").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG4_G = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG4-G").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG5_D = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG5-D").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG5_E = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG5-E").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG5_G = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG5-G").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         CMG6_E  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG6-E").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']  
#         CRA6_A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CRA6-A").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         EIG09_A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="EIG09-A").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         FIN13_K1 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN13-K1").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']   
#         FIN13_K2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN13-K2").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         FIN22_D1b = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN22-D1b").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         FIN22_D2a = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN22-D2a").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         FIN23_C1  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN23-C1").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']   
#         FIN9_C0301 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN9-C0301").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         FIN9_E02 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN9-E02").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         FIN9_F0201 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN9-F0201").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         FIN_F0201 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN-F0201").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         GEG02_A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-A").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         GEG02_B = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-B").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         GEG02_C   = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-C").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum'] 
#         GEG02_D = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-D").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         GEG02_E = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-E").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         GEG02_F = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-F").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         GEG02_G = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-G").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         GEG02_H = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-H").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         GEG02_K  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-K").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']     
#         GEG04_B = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG04-B").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         GENT_F2011 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GENT-F2011").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT2_D06_E = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-D06-E").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT2_D5_03  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-D5-03").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']  
#         NTT2_D5_05 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-D5-05").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT2_D6_03 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-D6-03").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT2_D6_05 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-D6-05").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT2_F4 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-F4").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT2_G4 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-G4").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT2_H3 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-H3").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT3_B5 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT3-B5").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT3_D5 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT3-D5").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT5_B05A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-B05A").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT5_B06 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-B06").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT5_C01  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-C01").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum'] 
#         NTT5_D01  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-D01").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']  
#         NTT5_D02 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-D02").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT5_E03 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-E03").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT5_E04 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-E04").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT5_G01 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-G01").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']    
#         NTT5_G02 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-G02").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT5_G03 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-G03").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT5_H01  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-H01").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']  
#         NTT5_H03 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-H03").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT5_I01 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-I01").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT5_I02 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-I02").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT5_I03 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-I03").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT5_J01  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-J01").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']  
#         NTT5_J02 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-J02").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT5_J03 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-J03").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT6_C = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT6-C").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         NTT7_E = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT7-E").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         OP12_A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="OP12-A").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         SG02_O = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-O").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         SG02_O2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-O2").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         SG02_P = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-P").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         SG02_Q = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-Q").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         SG02_Q2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-Q2").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         SG02_R = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-R").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         SG02_U = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-U").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         SG11_A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG11-A").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']
#         ST1 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="ST1").aggregate(Sum('DelcoGrossValue'))['DelcoGrossValue__sum']

#         reb_BB14_B10 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B10").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_BB14_B2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B2").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_BB14_B3 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B3").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_BB14_B4 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B4").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_BB14_B5 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B5").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_BB14_B6 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B6").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_BB14_B7 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B7").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_BB14_B8 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-B8").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_BB14_E = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="BB14-E").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMB4_B = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMB4-B").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG12_D = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG12-D").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_B1 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-B1").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_B3 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-B3").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_C1 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C1").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_C2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C2").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_C3 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C3").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_C4 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C4").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_C5_B = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C5-B").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_C5_C = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C5-C").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_C5_G = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-C5-G").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum'] 
#         reb_CMG2_D1 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-D1").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_D2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-D2").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_D3 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-D3").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_E2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-E2").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_E3 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-E3").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_F1  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-F1").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']  
#         reb_CMG2_F2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-F2").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG2_F3  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG2-F3").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']  
#         reb_CMG3_A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG3-A").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG4_B = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG4-B").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG4_C = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG4-C").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG4_D = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG4-D").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG4_E = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG4-E").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG4_F = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG4-F").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG4_G = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG4-G").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG5_D = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG5-D").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG5_E = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG5-E").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG5_G = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG5-G").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_CMG6_E  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CMG6-E").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']  
#         reb_CRA6_A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="CRA6-A").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_EIG09_A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="EIG09-A").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_FIN13_K1 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN13-K1").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']   
#         reb_FIN13_K2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN13-K2").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_FIN22_D1b = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN22-D1b").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_FIN22_D2a = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN22-D2a").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_FIN23_C1  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN23-C1").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']   
#         reb_FIN9_C0301 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN9-C0301").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_FIN9_E02 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN9-E02").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_FIN9_F0201 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN9-F0201").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_FIN_F0201 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="FIN-F0201").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_GEG02_A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-A").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_GEG02_B = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-B").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_GEG02_C   = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-C").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum'] 
#         reb_GEG02_D = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-D").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_GEG02_E = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-E").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_GEG02_F = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-F").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_GEG02_G = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-G").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_GEG02_H = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-H").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_GEG02_K  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG02-K").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']     
#         reb_GEG04_B = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GEG04-B").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_GENT_F2011 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="GENT-F2011").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT2_D06_E = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-D06-E").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT2_D5_03  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-D5-03").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']  
#         reb_NTT2_D5_05 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-D5-05").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT2_D6_03 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-D6-03").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT2_D6_05 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-D6-05").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT2_F4 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-F4").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT2_G4 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-G4").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT2_H3 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT2-H3").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT3_B5 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT3-B5").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT3_D5 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT3-D5").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT5_B05A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-B05A").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT5_B06 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-B06").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT5_C01  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-C01").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum'] 
#         reb_NTT5_D01  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-D01").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']  
#         reb_NTT5_D02 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-D02").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT5_E03 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-E03").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT5_E04 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-E04").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT5_G01 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-G01").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']    
#         reb_NTT5_G02 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-G02").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT5_G03 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-G03").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT5_H01  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-H01").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']  
#         reb_NTT5_H03 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-H03").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT5_I01 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-I01").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT5_I02 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-I02").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT5_I03 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-I03").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT5_J01  = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-J01").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']  
#         reb_NTT5_J02 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-J02").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT5_J03 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT5-J03").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT6_C = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT6-C").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_NTT7_E = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="NTT7-E").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_OP12_A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="OP12-A").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_SG02_O = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-O").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_SG02_O2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-O2").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_SG02_P = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-P").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_SG02_Q = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-Q").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_SG02_Q2 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-Q2").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_SG02_R = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-R").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_SG02_U = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG02-U").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_SG11_A = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="SG11-A").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']
#         reb_ST1 = shell_report.objects.filter(Trx_Invoice_Date__year=date.year, 
#             Trx_Invoice_Date__month=date.month, Trx_Transaction_Provider_Description='Shell Philippines', Cost_Center="ST1").aggregate(Sum('RebateCustAmount'))['RebateCustAmount__sum']

#         shell_data = [
#         BB14_B10, BB14_B2, BB14_B3, BB14_B4, BB14_B5, BB14_B6, BB14_B7, BB14_B8, BB14_E, CMB4_B
#         ]
#         shell_reb_data = [
#         reb_BB14_B10,reb_BB14_B2,reb_BB14_B3,reb_BB14_B4,reb_BB14_B5,reb_BB14_B6,reb_BB14_B7,reb_BB14_B8,reb_BB14_E,reb_CMB4_B      
#         ]
#         shell_label =[
#         "BB14-B10", "BB14-B2", "BB14-B3", "BB14-B4", "BB14-B5", "BB14-B6", "BB14-B7", "BB14-B8", "BB14-E", "CMB4-B"
#         ]
#         shell_report_data = {
#                     "shell_data": shell_data,
#                     "shell_label":shell_label,
#                     "shell_reb_data":shell_reb_data,
#             }
#         # print(shell_data)
#         return Response(shell_report_data)