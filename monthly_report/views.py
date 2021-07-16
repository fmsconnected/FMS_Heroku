from django.shortcuts import render,HttpResponseRedirect,HttpResponse, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment
from openpyxl.styles.colors import Color
import datetime
from datetime import date, timedelta
from django.urls import reverse_lazy

from .serializers import (
    petron_report_Serializer
    )
from . models import Petron_report
from rest_framework import viewsets
from django.views.generic import (
                				CreateView,
                				ListView,
                				UpdateView,
                				DetailView,
                                DeleteView,
                				)
from django.db.models import Sum
from .serializers import petron_report_Serializer
from . forms import petron_form


def monthly_report_jan(request):
	jan_data = Petron_report.objects.all()
	return render(request, 'monthly_report/petron_report.html',{'title':'Report','jan_data':jan_data})


class petronViewSet(viewsets.ModelViewSet):
    queryset = Petron_report.objects.all().order_by('id')
    serializer_class = petron_report_Serializer

class petron_create(CreateView):
    model = Petron_report
    form_class = petron_form
    template_name = 'monthly_report/petron_create.html'

class petron_update(UpdateView):
    model = Petron_report
    form_class = petron_form
    template_name = 'monthly_report/petron_create.html'

class petron_details(DetailView):
    model = Petron_report
    template_name = 'monthly_report/petron_detail.html'

class petron_delete(DeleteView):
    model = Petron_report
    success_url = reverse_lazy('jan_monthly_report')
    template_name = 'monthly_report/petron_delete.html'

def monthly_report_jan_summary(request):

    date = datetime.datetime.today()
    ## ProductAmount ####
    BB14_B1 = Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B1").aggregate(Sum('ProductAmount'))
    BB14_B10= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B10").aggregate(Sum('ProductAmount'))
    BB14_B11= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B11").aggregate(Sum('ProductAmount'))
    BB14_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B2").aggregate(Sum('ProductAmount'))
    BB14_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B3").aggregate(Sum('ProductAmount'))
    BB14_B4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B4").aggregate(Sum('ProductAmount'))
    BB14_B5= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B5").aggregate(Sum('ProductAmount'))
    BB14_B6= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B6").aggregate(Sum('ProductAmount'))
    BB14_B7= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B7").aggregate(Sum('ProductAmount'))
    BB14_B8= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B8").aggregate(Sum('ProductAmount'))
    BB14_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-C").aggregate(Sum('ProductAmount'))
    BB14_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-E").aggregate(Sum('ProductAmount'))
    CMG12_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG12-C").aggregate(Sum('ProductAmount'))
    CMG12_D= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG12-D").aggregate(Sum('ProductAmount'))
    CMG2_B1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B1").aggregate(Sum('ProductAmount'))
    CMG2_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B2").aggregate(Sum('ProductAmount'))
    CMG2_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B3").aggregate(Sum('ProductAmount'))
    CMG2_C1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C1").aggregate(Sum('ProductAmount'))
    CMG2_C2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C2").aggregate(Sum('ProductAmount'))
    CMG2_C3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C3").aggregate(Sum('ProductAmount'))
    CMG2_C4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C4").aggregate(Sum('ProductAmount'))
    CMG2_C5_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C5-C").aggregate(Sum('ProductAmount'))
    CMG2_D1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D1").aggregate(Sum('ProductAmount'))
    CMG2_D2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D2").aggregate(Sum('ProductAmount'))
    CMG2_D3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D3").aggregate(Sum('ProductAmount'))
    CMG2_E1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E1").aggregate(Sum('ProductAmount'))
    CMG2_E2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E2").aggregate(Sum('ProductAmount'))
    CMG2_E3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E3").aggregate(Sum('ProductAmount'))
    CMG2_F1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F1").aggregate(Sum('ProductAmount'))
    CMG2_F2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F2").aggregate(Sum('ProductAmount'))
    CMG2_F3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F3").aggregate(Sum('ProductAmount'))
    CMG3_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG3-A").aggregate(Sum('ProductAmount'))
    CMG4_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B").aggregate(Sum('ProductAmount'))
    CMG4_B15= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B15").aggregate(Sum('ProductAmount'))
    CMG4_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B2").aggregate(Sum('ProductAmount'))
    CMG4_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-E").aggregate(Sum('ProductAmount'))
    CMG4_F= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-F").aggregate(Sum('ProductAmount'))
    CMG4_G= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-G").aggregate(Sum('ProductAmount'))
    CMG5_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-B").aggregate(Sum('ProductAmount'))
    CMG5_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-E").aggregate(Sum('ProductAmount'))
    CMG5_G= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-G").aggregate(Sum('ProductAmount'))
    CMG6_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-B").aggregate(Sum('ProductAmount'))
    CMG6_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-C").aggregate(Sum('ProductAmount'))
    CMG6_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-E").aggregate(Sum('ProductAmount'))
    CMG7_F= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG7-F").aggregate(Sum('ProductAmount'))
    CMG8_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG8-B").aggregate(Sum('ProductAmount'))
    CRA6_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CRA6-A").aggregate(Sum('ProductAmount'))
    FIN23_C1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C1").aggregate(Sum('ProductAmount'))
    FIN23_C10= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C10").aggregate(Sum('ProductAmount'))
    FIN23_C4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C4").aggregate(Sum('ProductAmount'))
    FIN23_C9= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C9").aggregate(Sum('ProductAmount'))
    FIN9_C0201= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN9-C0201").aggregate(Sum('ProductAmount'))
    FIN9_C0301= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN9-C0301").aggregate(Sum('ProductAmount'))
    GEG02_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-B").aggregate(Sum('ProductAmount'))
    GEG02_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-C").aggregate(Sum('ProductAmount'))
    GEG02_D= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-D").aggregate(Sum('ProductAmount'))
    GEG02_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-E").aggregate(Sum('ProductAmount'))
    GEG02_G= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-G").aggregate(Sum('ProductAmount'))
    GEG02_H= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-H").aggregate(Sum('ProductAmount'))
    GEG02_I= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-I").aggregate(Sum('ProductAmount'))
    GEG02_K= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-K").aggregate(Sum('ProductAmount'))
    GEG02_L= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-L").aggregate(Sum('ProductAmount'))
    GEG04_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-B3").aggregate(Sum('ProductAmount'))
    GEG05_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-E").aggregate(Sum('ProductAmount'))
    GEG09_D= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-D").aggregate(Sum('ProductAmount'))
    GRTM_C503= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GRTM-C503").aggregate(Sum('ProductAmount'))
    ISG18_C2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="ISG18-C2").aggregate(Sum('ProductAmount'))
    NTT11_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT11-E").aggregate(Sum('ProductAmount'))
    NTT2_C3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C3").aggregate(Sum('ProductAmount'))
    NTT2_C5= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C5").aggregate(Sum('ProductAmount'))
    NTT2_C6= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C6").aggregate(Sum('ProductAmount'))
    NTT2_D01_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D01-A").aggregate(Sum('ProductAmount'))
    NTT2_D08_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D08-C").aggregate(Sum('ProductAmount'))
    NTT2_D1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D1").aggregate(Sum('ProductAmount'))
    NTT2_D2_02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-02").aggregate(Sum('ProductAmount'))
    NTT2_D2_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-03").aggregate(Sum('ProductAmount'))
    NTT2_D2_05= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-05").aggregate(Sum('ProductAmount'))
    NTT2_D3_02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-02").aggregate(Sum('ProductAmount'))
    NTT2_D3_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-03").aggregate(Sum('ProductAmount'))
    NTT2_D3_04= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-04").aggregate(Sum('ProductAmount'))
    NTT2_D3_06= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-06").aggregate(Sum('ProductAmount'))
    NTT2_D4_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D4-03").aggregate(Sum('ProductAmount'))
    NTT2_D5_02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D5-02").aggregate(Sum('ProductAmount'))
    NTT2_D5_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D5-03").aggregate(Sum('ProductAmount'))
    NTT2_D6= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D6").aggregate(Sum('ProductAmount'))
    NTT2_D6_06= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D6-06").aggregate(Sum('ProductAmount'))
    NTT2_D7_01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-01").aggregate(Sum('ProductAmount'))
    NTT2_D7_02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-02").aggregate(Sum('ProductAmount'))
    NTT2_D7_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-03").aggregate(Sum('ProductAmount'))
    NTT2_E2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-E2").aggregate(Sum('ProductAmount'))
    NTT2_E3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-E3").aggregate(Sum('ProductAmount'))
    NTT2_F3A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3A").aggregate(Sum('ProductAmount'))
    NTT2_F3B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3B").aggregate(Sum('ProductAmount'))
    NTT2_F3D= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3D").aggregate(Sum('ProductAmount'))
    NTT2_F3E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3E").aggregate(Sum('ProductAmount'))
    NTT2_G2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-G2").aggregate(Sum('ProductAmount'))
    NTT2_G4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-G4").aggregate(Sum('ProductAmount'))
    NTT3_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-A").aggregate(Sum('ProductAmount'))
    NTT3_B5= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-B5").aggregate(Sum('ProductAmount'))
    NTT3_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-C").aggregate(Sum('ProductAmount'))
    NTT3_D2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D2").aggregate(Sum('ProductAmount'))
    NTT3_D3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D3").aggregate(Sum('ProductAmount'))
    NTT3_D4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D4").aggregate(Sum('ProductAmount'))
    NTT3_D5= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D5").aggregate(Sum('ProductAmount'))
    NTT5_A01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-A01").aggregate(Sum('ProductAmount'))
    NTT5_B02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-B02").aggregate(Sum('ProductAmount'))
    NTT5_B06= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-B06").aggregate(Sum('ProductAmount'))
    NTT5_C01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-C01").aggregate(Sum('ProductAmount'))
    NTT5_D01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D01").aggregate(Sum('ProductAmount'))
    NTT5_D02A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D02A").aggregate(Sum('ProductAmount'))
    NTT5_D02B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D02B").aggregate(Sum('ProductAmount'))
    NTT5_E03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-E03").aggregate(Sum('ProductAmount'))
    NTT5_E04= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-E04").aggregate(Sum('ProductAmount'))
    NTT5_F01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F01").aggregate(Sum('ProductAmount'))
    NTT5_F02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F02").aggregate(Sum('ProductAmount'))
    NTT5_F03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F03").aggregate(Sum('ProductAmount'))
    NTT5_G= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G").aggregate(Sum('ProductAmount'))
    NTT5_G01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G01").aggregate(Sum('ProductAmount'))
    NTT5_G02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G02").aggregate(Sum('ProductAmount'))
    NTT5_G03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G03").aggregate(Sum('ProductAmount'))
    NTT5_H01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-H01").aggregate(Sum('ProductAmount'))
    NTT5_H03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-H03").aggregate(Sum('ProductAmount'))
    NTT5_I01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-I01").aggregate(Sum('ProductAmount'))
    NTT5_I03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-I03").aggregate(Sum('ProductAmount'))
    NTT5_J01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-J01").aggregate(Sum('ProductAmount'))
    NTT5_J03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-J03").aggregate(Sum('ProductAmount'))
    OP12_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="OP12-A").aggregate(Sum('ProductAmount'))
    OP20_F1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="OP20-F1").aggregate(Sum('ProductAmount'))
    SG02_O= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-O").aggregate(Sum('ProductAmount'))
    SG02_P= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-P").aggregate(Sum('ProductAmount'))
    SG02_Q= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-Q").aggregate(Sum('ProductAmount'))
    SG02_R= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-R").aggregate(Sum('ProductAmount'))
    SG02_U= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('ProductAmount'))
    GEG02_F= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('ProductAmount'))
    GRTM_C503= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('ProductAmount'))
    GEG04_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('ProductAmount'))
    

    ## ProductAmount end ####

    ##Discount_Amount

    dis_BB14_B1 = Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B1").aggregate(Sum('DiscountAmount'))
    dis_BB14_B10= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B10").aggregate(Sum('DiscountAmount'))
    dis_BB14_B11= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B11").aggregate(Sum('DiscountAmount'))
    dis_BB14_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B2").aggregate(Sum('DiscountAmount'))
    dis_BB14_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B3").aggregate(Sum('DiscountAmount'))
    dis_BB14_B4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B4").aggregate(Sum('DiscountAmount'))
    dis_BB14_B5= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B5").aggregate(Sum('DiscountAmount'))
    dis_BB14_B6= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B6").aggregate(Sum('DiscountAmount'))
    dis_BB14_B7= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B7").aggregate(Sum('DiscountAmount'))
    dis_BB14_B8= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B8").aggregate(Sum('DiscountAmount'))
    dis_BB14_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-C").aggregate(Sum('DiscountAmount'))
    dis_BB14_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-E").aggregate(Sum('DiscountAmount'))
    dis_CMG12_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG12-C").aggregate(Sum('DiscountAmount'))
    dis_CMG12_D= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG12-D").aggregate(Sum('DiscountAmount'))
    dis_CMG2_B1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B1").aggregate(Sum('DiscountAmount'))
    dis_CMG2_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B2").aggregate(Sum('DiscountAmount'))
    dis_CMG2_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B3").aggregate(Sum('DiscountAmount'))
    dis_CMG2_C1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C1").aggregate(Sum('DiscountAmount'))
    dis_CMG2_C2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C2").aggregate(Sum('DiscountAmount'))
    dis_CMG2_C3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C3").aggregate(Sum('DiscountAmount'))
    dis_CMG2_C4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C4").aggregate(Sum('DiscountAmount'))
    dis_CMG2_C5_C= Petron_report.objects.filter(StatementDate__year=date.year, 
       StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C5-C").aggregate(Sum('DiscountAmount'))
    dis_CMG2_D1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D1").aggregate(Sum('DiscountAmount'))
    dis_CMG2_D2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D2").aggregate(Sum('DiscountAmount'))
    dis_CMG2_D3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D3").aggregate(Sum('DiscountAmount'))
    dis_CMG2_E1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E1").aggregate(Sum('DiscountAmount'))
    dis_CMG2_E2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E2").aggregate(Sum('DiscountAmount'))
    dis_CMG2_E3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E3").aggregate(Sum('DiscountAmount'))
    dis_CMG2_F1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F1").aggregate(Sum('DiscountAmount'))
    dis_CMG2_F2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F2").aggregate(Sum('DiscountAmount'))
    dis_CMG2_F3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F3").aggregate(Sum('DiscountAmount'))
    dis_CMG3_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG3-A").aggregate(Sum('DiscountAmount'))
    dis_CMG4_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B").aggregate(Sum('DiscountAmount'))
    dis_CMG4_B15= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B15").aggregate(Sum('DiscountAmount'))
    dis_CMG4_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B2").aggregate(Sum('DiscountAmount'))
    dis_CMG4_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-E").aggregate(Sum('DiscountAmount'))
    dis_CMG4_F= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-F").aggregate(Sum('DiscountAmount'))
    dis_CMG4_G= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-G").aggregate(Sum('DiscountAmount'))
    dis_CMG5_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-B").aggregate(Sum('DiscountAmount'))
    dis_CMG5_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-E").aggregate(Sum('DiscountAmount'))
    dis_CMG5_G= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-G").aggregate(Sum('DiscountAmount'))
    dis_CMG6_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-B").aggregate(Sum('DiscountAmount'))
    dis_CMG6_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-C").aggregate(Sum('DiscountAmount'))
    dis_CMG6_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-E").aggregate(Sum('DiscountAmount'))
    dis_CMG7_F= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG7-F").aggregate(Sum('DiscountAmount'))
    dis_CMG8_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG8-B").aggregate(Sum('DiscountAmount'))
    dis_CRA6_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CRA6-A").aggregate(Sum('DiscountAmount'))
    dis_FIN23_C1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C1").aggregate(Sum('DiscountAmount'))
    dis_FIN23_C10= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C10").aggregate(Sum('DiscountAmount'))
    dis_FIN23_C4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C4").aggregate(Sum('DiscountAmount'))
    dis_FIN23_C9= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C9").aggregate(Sum('DiscountAmount'))
    dis_FIN9_C0201= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN9-C0201").aggregate(Sum('DiscountAmount'))
    dis_FIN9_C0301= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN9-C0301").aggregate(Sum('DiscountAmount'))
    dis_GEG02_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-B").aggregate(Sum('DiscountAmount'))
    dis_GEG02_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-C").aggregate(Sum('DiscountAmount'))
    dis_GEG02_D= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-D").aggregate(Sum('DiscountAmount'))
    dis_GEG02_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-E").aggregate(Sum('DiscountAmount'))
    dis_GEG02_G= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-G").aggregate(Sum('DiscountAmount'))
    dis_GEG02_H= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-H").aggregate(Sum('DiscountAmount'))
    dis_GEG02_I= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-I").aggregate(Sum('DiscountAmount'))
    dis_GEG02_K= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-K").aggregate(Sum('DiscountAmount'))
    dis_GEG02_L= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-L").aggregate(Sum('DiscountAmount'))
    dis_GEG04_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-B3").aggregate(Sum('DiscountAmount'))
    dis_GEG05_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-E").aggregate(Sum('DiscountAmount'))
    dis_GEG09_D= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-D").aggregate(Sum('DiscountAmount'))
    dis_GRTM_C503= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GRTM-C503").aggregate(Sum('DiscountAmount'))
    dis_ISG18_C2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="ISG18-C2").aggregate(Sum('DiscountAmount'))
    dis_NTT11_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT11-E").aggregate(Sum('DiscountAmount'))
    dis_NTT2_C3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C3").aggregate(Sum('DiscountAmount'))
    dis_NTT2_C5= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C5").aggregate(Sum('DiscountAmount'))
    dis_NTT2_C6= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C6").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D01_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D01-A").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D08_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D08-C").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D1").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D2_02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-02").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D2_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-03").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D2_05= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-05").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D3_02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-02").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D3_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-03").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D3_04= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-04").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D3_06= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-06").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D4_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D4-03").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D5_02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D5-02").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D5_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D5-03").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D6= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D6").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D6_06= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D6-06").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D7_01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-01").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D7_02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-02").aggregate(Sum('DiscountAmount'))
    dis_NTT2_D7_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-03").aggregate(Sum('DiscountAmount'))
    dis_NTT2_E2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-E2").aggregate(Sum('DiscountAmount'))
    dis_NTT2_E3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-E3").aggregate(Sum('DiscountAmount'))
    dis_NTT2_F3A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3A").aggregate(Sum('DiscountAmount'))
    dis_NTT2_F3B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3B").aggregate(Sum('DiscountAmount'))
    dis_NTT2_F3D= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3D").aggregate(Sum('DiscountAmount'))
    dis_NTT2_F3E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3E").aggregate(Sum('DiscountAmount'))
    dis_NTT2_G2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-G2").aggregate(Sum('DiscountAmount'))
    dis_NTT2_G4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-G4").aggregate(Sum('DiscountAmount'))
    dis_NTT3_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-A").aggregate(Sum('DiscountAmount'))
    dis_NTT3_B5= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-B5").aggregate(Sum('DiscountAmount'))
    dis_NTT3_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-C").aggregate(Sum('DiscountAmount'))
    dis_NTT3_D2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D2").aggregate(Sum('DiscountAmount'))
    dis_NTT3_D3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D3").aggregate(Sum('DiscountAmount'))
    dis_NTT3_D4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D4").aggregate(Sum('DiscountAmount'))
    dis_NTT3_D5= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D5").aggregate(Sum('DiscountAmount'))
    dis_NTT5_A01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-A01").aggregate(Sum('DiscountAmount'))
    dis_NTT5_B02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-B02").aggregate(Sum('DiscountAmount'))
    dis_NTT5_B06= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-B06").aggregate(Sum('DiscountAmount'))
    dis_NTT5_C01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-C01").aggregate(Sum('DiscountAmount'))
    dis_NTT5_D01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D01").aggregate(Sum('DiscountAmount'))
    dis_NTT5_D02A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D02A").aggregate(Sum('DiscountAmount'))
    dis_NTT5_D02B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D02B").aggregate(Sum('DiscountAmount'))
    dis_NTT5_E03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-E03").aggregate(Sum('DiscountAmount'))
    dis_NTT5_E04= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-E04").aggregate(Sum('DiscountAmount'))
    dis_NTT5_F01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F01").aggregate(Sum('DiscountAmount'))
    dis_NTT5_F02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F02").aggregate(Sum('DiscountAmount'))
    dis_NTT5_F03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F03").aggregate(Sum('DiscountAmount'))
    dis_NTT5_G= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G").aggregate(Sum('DiscountAmount'))
    dis_NTT5_G01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G01").aggregate(Sum('DiscountAmount'))
    dis_NTT5_G02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G02").aggregate(Sum('DiscountAmount'))
    dis_NTT5_G03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G03").aggregate(Sum('DiscountAmount'))
    dis_NTT5_H01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-H01").aggregate(Sum('DiscountAmount'))
    dis_NTT5_H03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-H03").aggregate(Sum('DiscountAmount'))
    dis_NTT5_I01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-I01").aggregate(Sum('DiscountAmount'))
    dis_NTT5_I03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-I03").aggregate(Sum('DiscountAmount'))
    dis_NTT5_J01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-J01").aggregate(Sum('DiscountAmount'))
    dis_NTT5_J03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-J03").aggregate(Sum('DiscountAmount'))
    dis_OP12_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="OP12-A").aggregate(Sum('DiscountAmount'))
    dis_OP20_F1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="OP20-F1").aggregate(Sum('DiscountAmount'))
    dis_SG02_O= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-O").aggregate(Sum('DiscountAmount'))
    dis_SG02_P= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-P").aggregate(Sum('DiscountAmount'))
    dis_SG02_Q= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-Q").aggregate(Sum('DiscountAmount'))
    dis_SG02_R= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-R").aggregate(Sum('DiscountAmount'))
    dis_SG02_U= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('DiscountAmount'))
    dis_GEG02_F= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('DiscountAmount'))
    dis_GRTM_C503= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('DiscountAmount'))
    dis_GEG04_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('DiscountAmount'))
    
    ## Discount_Amount end ######

    ### Net Amount #####
    net_BB14_B1 = Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B1").aggregate(Sum('NetAmount'))
    net_BB14_B10= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B10").aggregate(Sum('NetAmount'))
    net_BB14_B11= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B11").aggregate(Sum('NetAmount'))
    net_BB14_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B2").aggregate(Sum('NetAmount'))
    net_BB14_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B3").aggregate(Sum('NetAmount'))
    net_BB14_B4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B4").aggregate(Sum('NetAmount'))
    net_BB14_B5= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B5").aggregate(Sum('NetAmount'))
    net_BB14_B6= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B6").aggregate(Sum('NetAmount'))
    net_BB14_B7= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B7").aggregate(Sum('NetAmount'))
    net_BB14_B8= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-B8").aggregate(Sum('NetAmount'))
    net_BB14_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-C").aggregate(Sum('NetAmount'))
    net_BB14_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="BB14-E").aggregate(Sum('NetAmount'))
    net_CMG12_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG12-C").aggregate(Sum('NetAmount'))
    net_CMG12_D= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG12-D").aggregate(Sum('NetAmount'))
    net_CMG2_B1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B1").aggregate(Sum('NetAmount'))
    net_CMG2_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B2").aggregate(Sum('NetAmount'))
    net_CMG2_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-B3").aggregate(Sum('NetAmount'))
    net_CMG2_C1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C1").aggregate(Sum('NetAmount'))
    net_CMG2_C2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C2").aggregate(Sum('NetAmount'))
    net_CMG2_C3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C3").aggregate(Sum('NetAmount'))
    net_CMG2_C4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C4").aggregate(Sum('NetAmount'))
    net_CMG2_C5_C= Petron_report.objects.filter(StatementDate__year=date.year, 
       StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-C5-C").aggregate(Sum('NetAmount'))
    net_CMG2_D1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D1").aggregate(Sum('NetAmount'))
    net_CMG2_D2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D2").aggregate(Sum('NetAmount'))
    net_CMG2_D3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-D3").aggregate(Sum('NetAmount'))
    net_CMG2_E1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E1").aggregate(Sum('NetAmount'))
    net_CMG2_E2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E2").aggregate(Sum('NetAmount'))
    net_CMG2_E3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-E3").aggregate(Sum('NetAmount'))
    net_CMG2_F1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F1").aggregate(Sum('NetAmount'))
    net_CMG2_F2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F2").aggregate(Sum('NetAmount'))
    net_CMG2_F3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG2-F3").aggregate(Sum('NetAmount'))
    net_CMG3_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG3-A").aggregate(Sum('NetAmount'))
    net_CMG4_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B").aggregate(Sum('NetAmount'))
    net_CMG4_B15= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B15").aggregate(Sum('NetAmount'))
    net_CMG4_B2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-B2").aggregate(Sum('NetAmount'))
    net_CMG4_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-E").aggregate(Sum('NetAmount'))
    net_CMG4_F= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-F").aggregate(Sum('NetAmount'))
    net_CMG4_G= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG4-G").aggregate(Sum('NetAmount'))
    net_CMG5_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-B").aggregate(Sum('NetAmount'))
    net_CMG5_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-E").aggregate(Sum('NetAmount'))
    net_CMG5_G= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG5-G").aggregate(Sum('NetAmount'))
    net_CMG6_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-B").aggregate(Sum('NetAmount'))
    net_CMG6_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-C").aggregate(Sum('NetAmount'))
    net_CMG6_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG6-E").aggregate(Sum('NetAmount'))
    net_CMG7_F= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG7-F").aggregate(Sum('NetAmount'))
    net_CMG8_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CMG8-B").aggregate(Sum('NetAmount'))
    net_CRA6_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="CRA6-A").aggregate(Sum('NetAmount'))
    net_FIN23_C1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C1").aggregate(Sum('NetAmount'))
    net_FIN23_C10= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C10").aggregate(Sum('NetAmount'))
    net_FIN23_C4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C4").aggregate(Sum('NetAmount'))
    net_FIN23_C9= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN23-C9").aggregate(Sum('NetAmount'))
    net_FIN9_C0201= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN9-C0201").aggregate(Sum('NetAmount'))
    net_FIN9_C0301= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="FIN9-C0301").aggregate(Sum('NetAmount'))
    net_GEG02_B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-B").aggregate(Sum('NetAmount'))
    net_GEG02_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-C").aggregate(Sum('NetAmount'))
    net_GEG02_D= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-D").aggregate(Sum('NetAmount'))
    net_GEG02_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-E").aggregate(Sum('NetAmount'))
    net_GEG02_G= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-G").aggregate(Sum('NetAmount'))
    net_GEG02_H= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-H").aggregate(Sum('NetAmount'))
    net_GEG02_I= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-I").aggregate(Sum('NetAmount'))
    net_GEG02_K= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-K").aggregate(Sum('NetAmount'))
    net_GEG02_L= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-L").aggregate(Sum('NetAmount'))
    net_GEG04_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-B3").aggregate(Sum('NetAmount'))
    net_GEG05_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-E").aggregate(Sum('NetAmount'))
    net_GEG09_D= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GEG02-D").aggregate(Sum('NetAmount'))
    net_GRTM_C503= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="GRTM-C503").aggregate(Sum('NetAmount'))
    net_ISG18_C2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="ISG18-C2").aggregate(Sum('NetAmount'))
    net_NTT11_E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT11-E").aggregate(Sum('NetAmount'))
    net_NTT2_C3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C3").aggregate(Sum('NetAmount'))
    net_NTT2_C5= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C5").aggregate(Sum('NetAmount'))
    net_NTT2_C6= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-C6").aggregate(Sum('NetAmount'))
    net_NTT2_D01_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D01-A").aggregate(Sum('NetAmount'))
    net_NTT2_D08_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D08-C").aggregate(Sum('NetAmount'))
    net_NTT2_D1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D1").aggregate(Sum('NetAmount'))
    net_NTT2_D2_02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-02").aggregate(Sum('NetAmount'))
    net_NTT2_D2_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-03").aggregate(Sum('NetAmount'))
    net_NTT2_D2_05= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D2-05").aggregate(Sum('NetAmount'))
    net_NTT2_D3_02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-02").aggregate(Sum('NetAmount'))
    net_NTT2_D3_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-03").aggregate(Sum('NetAmount'))
    net_NTT2_D3_04= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-04").aggregate(Sum('NetAmount'))
    net_NTT2_D3_06= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D3-06").aggregate(Sum('NetAmount'))
    net_NTT2_D4_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D4-03").aggregate(Sum('NetAmount'))
    net_NTT2_D5_02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D5-02").aggregate(Sum('NetAmount'))
    net_NTT2_D5_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D5-03").aggregate(Sum('NetAmount'))
    net_NTT2_D6= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D6").aggregate(Sum('NetAmount'))
    net_NTT2_D6_06= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D6-06").aggregate(Sum('NetAmount'))
    net_NTT2_D7_01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-01").aggregate(Sum('NetAmount'))
    net_NTT2_D7_02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-02").aggregate(Sum('NetAmount'))
    net_NTT2_D7_03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-D7-03").aggregate(Sum('NetAmount'))
    net_NTT2_E2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-E2").aggregate(Sum('NetAmount'))
    net_NTT2_E3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-E3").aggregate(Sum('NetAmount'))
    net_NTT2_F3A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3A").aggregate(Sum('NetAmount'))
    net_NTT2_F3B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3B").aggregate(Sum('NetAmount'))
    net_NTT2_F3D= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3D").aggregate(Sum('NetAmount'))
    net_NTT2_F3E= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-F3E").aggregate(Sum('NetAmount'))
    net_NTT2_G2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-G2").aggregate(Sum('NetAmount'))
    net_NTT2_G4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT2-G4").aggregate(Sum('NetAmount'))
    net_NTT3_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-A").aggregate(Sum('NetAmount'))
    net_NTT3_B5= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-B5").aggregate(Sum('NetAmount'))
    net_NTT3_C= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-C").aggregate(Sum('NetAmount'))
    net_NTT3_D2= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D2").aggregate(Sum('NetAmount'))
    net_NTT3_D3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D3").aggregate(Sum('NetAmount'))
    net_NTT3_D4= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D4").aggregate(Sum('NetAmount'))
    net_NTT3_D5= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT3-D5").aggregate(Sum('NetAmount'))
    net_NTT5_A01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-A01").aggregate(Sum('NetAmount'))
    net_NTT5_B02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-B02").aggregate(Sum('NetAmount'))
    net_NTT5_B06= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-B06").aggregate(Sum('NetAmount'))
    net_NTT5_C01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-C01").aggregate(Sum('NetAmount'))
    net_NTT5_D01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D01").aggregate(Sum('NetAmount'))
    net_NTT5_D02A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D02A").aggregate(Sum('NetAmount'))
    net_NTT5_D02B= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-D02B").aggregate(Sum('NetAmount'))
    net_NTT5_E03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-E03").aggregate(Sum('NetAmount'))
    net_NTT5_E04= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-E04").aggregate(Sum('NetAmount'))
    net_NTT5_F01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F01").aggregate(Sum('NetAmount'))
    net_NTT5_F02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F02").aggregate(Sum('NetAmount'))
    net_NTT5_F03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-F03").aggregate(Sum('NetAmount'))
    net_NTT5_G= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G").aggregate(Sum('NetAmount'))
    net_NTT5_G01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G01").aggregate(Sum('NetAmount'))
    net_NTT5_G02= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G02").aggregate(Sum('NetAmount'))
    net_NTT5_G03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-G03").aggregate(Sum('NetAmount'))
    net_NTT5_H01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-H01").aggregate(Sum('NetAmount'))
    net_NTT5_H03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-H03").aggregate(Sum('NetAmount'))
    net_NTT5_I01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-I01").aggregate(Sum('NetAmount'))
    net_NTT5_I03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-I03").aggregate(Sum('NetAmount'))
    net_NTT5_J01= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-J01").aggregate(Sum('NetAmount'))
    net_NTT5_J03= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="NTT5-J03").aggregate(Sum('NetAmount'))
    net_OP12_A= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="OP12-A").aggregate(Sum('NetAmount'))
    net_OP20_F1= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="OP20-F1").aggregate(Sum('NetAmount'))
    net_SG02_O= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-O").aggregate(Sum('NetAmount'))
    net_SG02_P= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-P").aggregate(Sum('NetAmount'))
    net_SG02_Q= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-Q").aggregate(Sum('NetAmount'))
    net_SG02_R= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-R").aggregate(Sum('NetAmount'))
    net_SG02_U= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('NetAmount'))
    net_GEG02_F= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('NetAmount'))
    net_GRTM_C503= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('NetAmount'))
    net_GEG04_B3= Petron_report.objects.filter(StatementDate__year=date.year, 
        StatementDate__month=date.month, Supplier='Petron', ChargingDepartment="SG02-U").aggregate(Sum('NetAmount'))

    ### Net Amount End#####
    
    return render(request,'monthly_report/petron_report_summary.html',{'title':'Petron Data', 'BB14_B1':BB14_B1,
    'BB14_B10':BB14_B10, 'BB14_B11':BB14_B11, 'BB14_B2':BB14_B2, 'BB14_B3':BB14_B3, 'BB14_B4':BB14_B4, 'BB14_B5':BB14_B5, 'BB14_B6':BB14_B6,
    'BB14_B7':BB14_B7, 'BB14_B8':BB14_B8, 'BB14_C':BB14_C, 'BB14_E':BB14_E, 'CMG12_C':CMG12_C, 
    'CMG12_D':CMG12_D, 'CMG2_B1':CMG2_B1, 'CMG2_B2':CMG2_B2, 'CMG2_B3':CMG2_B3, 'CMG2_C1':CMG2_C1, 'CMG2_C2':CMG2_C2, 
    'CMG2_C3':CMG2_C3, 'CMG2_C4':CMG2_C4, 'CMG2_C5_C':CMG2_C5_C, 'CMG2_D1':CMG2_D1, 'CMG2_D2':CMG2_D2, 'CMG2_D3':CMG2_D3, 'CMG2_E1':CMG2_E1, 
    'CMG2_E2':CMG2_E2, 'CMG2_E3':CMG2_E3, 'CMG2_F1':CMG2_F1, 'CMG2_F2':CMG2_F2, 'CMG2_F3':CMG2_F3, 'CMG3_A':CMG3_A, 'CMG4_B':CMG4_B, 
    'CMG4_B15':CMG4_B15, 'CMG4_B2':CMG4_B2, 'CMG4_E':CMG4_E, 'CMG4_F':CMG4_F, 'CMG4_G':CMG4_G, 'CMG5_B':CMG5_B, 'CMG5_E':CMG5_E, 
    'CMG5_G':CMG5_G, 'CMG6_B':CMG6_B, 'CMG6_C':CMG6_C, 'CMG6_E':CMG6_E, 'CMG7_F':CMG7_F, 'CMG8_B':CMG8_B, 'CRA6_A':CRA6_A, 'FIN23_C1':FIN23_C1, 
    'FIN23_C10':FIN23_C10, 'FIN23_C4':FIN23_C4, 'FIN23_C9':FIN23_C9, 'FIN9_C0201':FIN9_C0201, 'FIN9_C0301':FIN9_C0301, 'GEG02_B':GEG02_B, 
    'GEG02_C':GEG02_C, 'GEG02_D':GEG02_D, 'GEG02_E':GEG02_E, 'GEG02_G':GEG02_G, 'GEG02_H':GEG02_H, 'GEG02_I':GEG02_I, 'GEG02_K':GEG02_K, 
    'GEG02_L':GEG02_L, 'GEG04_B3':GEG04_B3, 'GEG05_E':GEG05_E, 'GEG09_D':GEG09_D, 'GRTM_C503':GRTM_C503, 'ISG18_C2':ISG18_C2, 'NTT11_E':NTT11_E, 
    'NTT2_C3':NTT2_C3, 'NTT2_C5':NTT2_C5, 'NTT2_C6':NTT2_C6, 'NTT2_D01_A':NTT2_D01_A, 'NTT2_D08_C':NTT2_D08_C, 'NTT2_D1':NTT2_D1, 'NTT2_D2_02':NTT2_D2_02, 
    'NTT2_D2_03':NTT2_D2_03, 'NTT2_D2_05':NTT2_D2_05, 'NTT2_D3_02':NTT2_D3_02, 'NTT2_D3_03':NTT2_D3_03, 'NTT2_D3_04':NTT2_D3_04, 'NTT2_D3_06':NTT2_D3_06, 
    'NTT2_D4_03':NTT2_D4_03, 'NTT2_D5_02':NTT2_D5_02, 'NTT2_D5_03':NTT2_D5_03, 'NTT2_D6':NTT2_D6, 'NTT2_D6_06':NTT2_D6_06, 'NTT2_D7_01':NTT2_D7_01, 
    'NTT2_D7_02':NTT2_D7_02, 'NTT2_D7_03':NTT2_D7_03, 'NTT2_E2':NTT2_E2, 'NTT2_E3':NTT2_E3, 'NTT2_F3A':NTT2_F3A, 'NTT2_F3B':NTT2_F3B, 'NTT2_F3D':NTT2_F3D, 
    'NTT2_F3E':NTT2_F3E, 'NTT2_G2':NTT2_G2, 'NTT2_G4':NTT2_G4, 'NTT3_A':NTT3_A, 'NTT3_B5':NTT3_B5, 'NTT3_C':NTT3_C, 'NTT3_D2':NTT3_D2, 'NTT3_D3':NTT3_D3, 
    'NTT3_D4':NTT3_D4, 'NTT3_D5':NTT3_D5, 'NTT5_A01':NTT5_A01, 'NTT5_B02':NTT5_B02, 'NTT5_B06':NTT5_B06, 'NTT5_C01':NTT5_C01, 'NTT5_D01':NTT5_D01, 
    'NTT5_D02A':NTT5_D02A, 'NTT5_D02B':NTT5_D02B, 'NTT5_E03':NTT5_E03, 'NTT5_E04':NTT5_E04, 'NTT5_F01':NTT5_F01, 'NTT5_F02':NTT5_F02, 'NTT5_F03':NTT5_F03, 
    'NTT5_G':NTT5_G, 'NTT5_G01':NTT5_G01, 'NTT5_G02':NTT5_G02, 'NTT5_G03':NTT5_G03, 'NTT5_H01':NTT5_H01, 'NTT5_H03':NTT5_H03, 'NTT5_I01':NTT5_I01, 
    'NTT5_I03':NTT5_I03, 'NTT5_J01':NTT5_J01, 'NTT5_J03':NTT5_J03, 'OP12_A':OP12_A, 'OP20_F1':OP20_F1, 'SG02_O':SG02_O, 'SG02_P':SG02_P, 'SG02_Q':SG02_Q, 
    'SG02_R':SG02_R, 'SG02_U':SG02_U, 'dis_BB14_B1':dis_BB14_B1,
    'dis_BB14_B10':dis_BB14_B10, 'dis_BB14_B11':dis_BB14_B11, 'dis_BB14_B2':dis_BB14_B2, 'dis_BB14_B3':dis_BB14_B3, 'dis_BB14_B4':dis_BB14_B4, 'dis_BB14_B5':dis_BB14_B5, 'dis_BB14_B6':dis_BB14_B6,
    'dis_BB14_B7':dis_BB14_B7, 'dis_BB14_B8':dis_BB14_B8, 'dis_BB14_C':dis_BB14_C, 'dis_BB14_E':dis_BB14_E, 'dis_CMG12_C':dis_CMG12_C, 
    'dis_CMG12_D':dis_CMG12_D, 'dis_CMG2_B1':dis_CMG2_B1, 'dis_CMG2_B2':dis_CMG2_B2, 'dis_CMG2_B3':dis_CMG2_B3, 'dis_CMG2_C1':dis_CMG2_C1, 'dis_CMG2_C2':dis_CMG2_C2, 
    'dis_CMG2_C3':dis_CMG2_C3, 'dis_CMG2_C4':dis_CMG2_C4, 'dis_CMG2_C5_C':dis_CMG2_C5_C, 'dis_CMG2_D1':dis_CMG2_D1, 'dis_CMG2_D2':dis_CMG2_D2, 'dis_CMG2_D3':dis_CMG2_D3, 'dis_CMG2_E1':dis_CMG2_E1, 
    'dis_CMG2_E2':dis_CMG2_E2, 'dis_CMG2_E3':dis_CMG2_E3, 'dis_CMG2_F1':dis_CMG2_F1, 'dis_CMG2_F2':dis_CMG2_F2, 'dis_CMG2_F3':dis_CMG2_F3, 'dis_CMG3_A':dis_CMG3_A, 'dis_CMG4_B':dis_CMG4_B, 
    'dis_CMG4_B15':dis_CMG4_B15, 'dis_CMG4_B2':dis_CMG4_B2, 'dis_CMG4_E':dis_CMG4_E, 'dis_CMG4_F':dis_CMG4_F, 'dis_CMG4_G':dis_CMG4_G, 'dis_CMG5_B':dis_CMG5_B, 'dis_CMG5_E':dis_CMG5_E, 
    'dis_CMG5_G':dis_CMG5_G, 'dis_CMG6_B':dis_CMG6_B, 'dis_CMG6_C':dis_CMG6_C, 'dis_CMG6_E':dis_CMG6_E, 'dis_CMG7_F':dis_CMG7_F, 'dis_CMG8_B':dis_CMG8_B, 'dis_CRA6_A':dis_CRA6_A, 'dis_FIN23_C1':dis_FIN23_C1, 
    'dis_FIN23_C10':dis_FIN23_C10, 'dis_FIN23_C4':dis_FIN23_C4, 'dis_FIN23_C9':dis_FIN23_C9, 'dis_FIN9_C0201':dis_FIN9_C0201, 'dis_FIN9_C0301':dis_FIN9_C0301, 'dis_GEG02_B':dis_GEG02_B, 
    'dis_GEG02_C':dis_GEG02_C, 'dis_GEG02_D':dis_GEG02_D, 'dis_GEG02_E':dis_GEG02_E, 'dis_GEG02_G':dis_GEG02_G, 'dis_GEG02_H':dis_GEG02_H, 'dis_GEG02_I':dis_GEG02_I, 'dis_GEG02_K':dis_GEG02_K, 
    'dis_GEG02_L':dis_GEG02_L, 'dis_GEG04_B3':dis_GEG04_B3, 'dis_GEG05_E':dis_GEG05_E, 'dis_GEG09_D':dis_GEG09_D, 'dis_GRTM_C503':dis_GRTM_C503, 'dis_ISG18_C2':dis_ISG18_C2, 'dis_NTT11_E':dis_NTT11_E, 
    'dis_NTT2_C3':dis_NTT2_C3, 'dis_NTT2_C5':dis_NTT2_C5, 'dis_NTT2_C6':dis_NTT2_C6, 'dis_NTT2_D01_A':dis_NTT2_D01_A, 'dis_NTT2_D08_C':dis_NTT2_D08_C, 'dis_NTT2_D1':dis_NTT2_D1, 'dis_NTT2_D2_02':dis_NTT2_D2_02, 
    'dis_NTT2_D2_03':dis_NTT2_D2_03, 'dis_NTT2_D2_05':dis_NTT2_D2_05, 'dis_NTT2_D3_02':dis_NTT2_D3_02, 'dis_NTT2_D3_03':dis_NTT2_D3_03, 'dis_NTT2_D3_04':dis_NTT2_D3_04, 'dis_NTT2_D3_06':dis_NTT2_D3_06, 
    'dis_NTT2_D4_03':dis_NTT2_D4_03, 'dis_NTT2_D5_02':dis_NTT2_D5_02, 'dis_NTT2_D5_03':dis_NTT2_D5_03, 'dis_NTT2_D6':dis_NTT2_D6, 'dis_NTT2_D6_06':dis_NTT2_D6_06, 'dis_NTT2_D7_01':dis_NTT2_D7_01, 
    'dis_NTT2_D7_02':dis_NTT2_D7_02, 'dis_NTT2_D7_03':dis_NTT2_D7_03, 'dis_NTT2_E2':dis_NTT2_E2, 'dis_NTT2_E3':dis_NTT2_E3, 'dis_NTT2_F3A':dis_NTT2_F3A, 'dis_NTT2_F3B':dis_NTT2_F3B, 'dis_NTT2_F3D':dis_NTT2_F3D, 
    'dis_NTT2_F3E':dis_NTT2_F3E, 'dis_NTT2_G2':dis_NTT2_G2, 'dis_NTT2_G4':dis_NTT2_G4, 'dis_NTT3_A':dis_NTT3_A, 'dis_NTT3_B5':dis_NTT3_B5, 'dis_NTT3_C':dis_NTT3_C, 'dis_NTT3_D2':dis_NTT3_D2, 'dis_NTT3_D3':dis_NTT3_D3, 
    'dis_NTT3_D4':dis_NTT3_D4, 'dis_NTT3_D5':dis_NTT3_D5, 'dis_NTT5_A01':dis_NTT5_A01, 'dis_NTT5_B02':dis_NTT5_B02, 'dis_NTT5_B06':dis_NTT5_B06, 'dis_NTT5_C01':dis_NTT5_C01, 'dis_NTT5_D01':dis_NTT5_D01, 
    'dis_NTT5_D02A':dis_NTT5_D02A, 'dis_NTT5_D02B':dis_NTT5_D02B, 'dis_NTT5_E03':dis_NTT5_E03, 'dis_NTT5_E04':dis_NTT5_E04, 'dis_NTT5_F01':dis_NTT5_F01, 'dis_NTT5_F02':dis_NTT5_F02, 'dis_NTT5_F03':dis_NTT5_F03, 
    'dis_NTT5_G':dis_NTT5_G, 'dis_NTT5_G01':dis_NTT5_G01, 'dis_NTT5_G02':dis_NTT5_G02, 'dis_NTT5_G03':dis_NTT5_G03, 'dis_NTT5_H01':dis_NTT5_H01, 'dis_NTT5_H03':dis_NTT5_H03, 'dis_NTT5_I01':dis_NTT5_I01, 
    'dis_NTT5_I03':dis_NTT5_I03, 'dis_NTT5_J01':dis_NTT5_J01, 'dis_NTT5_J03':dis_NTT5_J03, 'dis_OP12_A':dis_OP12_A, 'dis_OP20_F1':dis_OP20_F1, 'dis_SG02_O':dis_SG02_O, 'dis_SG02_P':dis_SG02_P, 'dis_SG02_Q':dis_SG02_Q, 
    'dis_SG02_R':dis_SG02_R, 'dis_SG02_U':dis_SG02_U, 'net_BB14_B1':net_BB14_B1,
    'net_BB14_B10':net_BB14_B10, 'net_BB14_B11':net_BB14_B11, 'net_BB14_B2':net_BB14_B2, 'net_BB14_B3':net_BB14_B3, 'net_BB14_B4':net_BB14_B4, 'net_BB14_B5':net_BB14_B5, 'net_BB14_B6':net_BB14_B6,
    'net_BB14_B7':net_BB14_B7, 'net_BB14_B8':net_BB14_B8, 'net_BB14_C':net_BB14_C, 'net_BB14_E':net_BB14_E, 'net_CMG12_C':net_CMG12_C, 
    'net_CMG12_D':net_CMG12_D, 'net_CMG2_B1':net_CMG2_B1, 'net_CMG2_B2':net_CMG2_B2, 'net_CMG2_B3':net_CMG2_B3, 'net_CMG2_C1':net_CMG2_C1, 'net_CMG2_C2':net_CMG2_C2, 
    'net_CMG2_C3':net_CMG2_C3, 'net_CMG2_C4':net_CMG2_C4, 'net_CMG2_C5_C':net_CMG2_C5_C, 'net_CMG2_D1':net_CMG2_D1, 'net_CMG2_D2':net_CMG2_D2, 'net_CMG2_D3':net_CMG2_D3, 'net_CMG2_E1':net_CMG2_E1, 
    'net_CMG2_E2':net_CMG2_E2, 'net_CMG2_E3':net_CMG2_E3, 'net_CMG2_F1':net_CMG2_F1, 'net_CMG2_F2':net_CMG2_F2, 'net_CMG2_F3':net_CMG2_F3, 'net_CMG3_A':net_CMG3_A, 'net_CMG4_B':net_CMG4_B, 
    'net_CMG4_B15':net_CMG4_B15, 'net_CMG4_B2':net_CMG4_B2, 'net_CMG4_E':net_CMG4_E, 'net_CMG4_F':net_CMG4_F, 'net_CMG4_G':net_CMG4_G, 'net_CMG5_B':net_CMG5_B, 'net_CMG5_E':net_CMG5_E, 
    'net_CMG5_G':net_CMG5_G, 'net_CMG6_B':net_CMG6_B, 'net_CMG6_C':net_CMG6_C, 'net_CMG6_E':net_CMG6_E, 'net_CMG7_F':net_CMG7_F, 'net_CMG8_B':net_CMG8_B, 'net_CRA6_A':net_CRA6_A, 'net_FIN23_C1':net_FIN23_C1, 
    'net_FIN23_C10':net_FIN23_C10, 'net_FIN23_C4':net_FIN23_C4, 'net_FIN23_C9':net_FIN23_C9, 'net_FIN9_C0201':net_FIN9_C0201, 'net_FIN9_C0301':net_FIN9_C0301, 'net_GEG02_B':net_GEG02_B, 
    'net_GEG02_C':net_GEG02_C, 'net_GEG02_D':net_GEG02_D, 'net_GEG02_E':net_GEG02_E, 'net_GEG02_G':net_GEG02_G, 'net_GEG02_H':net_GEG02_H, 'net_GEG02_I':net_GEG02_I, 'net_GEG02_K':net_GEG02_K, 
    'net_GEG02_L':net_GEG02_L, 'net_GEG04_B3':net_GEG04_B3, 'net_GEG05_E':net_GEG05_E, 'net_GEG09_D':net_GEG09_D, 'net_GRTM_C503':net_GRTM_C503, 'net_ISG18_C2':net_ISG18_C2, 'net_NTT11_E':net_NTT11_E, 
    'net_NTT2_C3':net_NTT2_C3, 'net_NTT2_C5':net_NTT2_C5, 'net_NTT2_C6':net_NTT2_C6, 'net_NTT2_D01_A':net_NTT2_D01_A, 'net_NTT2_D08_C':net_NTT2_D08_C, 'net_NTT2_D1':net_NTT2_D1, 'net_NTT2_D2_02':net_NTT2_D2_02, 
    'net_NTT2_D2_03':net_NTT2_D2_03, 'net_NTT2_D2_05':net_NTT2_D2_05, 'net_NTT2_D3_02':net_NTT2_D3_02, 'net_NTT2_D3_03':net_NTT2_D3_03, 'net_NTT2_D3_04':net_NTT2_D3_04, 'net_NTT2_D3_06':net_NTT2_D3_06, 
    'net_NTT2_D4_03':net_NTT2_D4_03, 'net_NTT2_D5_02':net_NTT2_D5_02, 'net_NTT2_D5_03':net_NTT2_D5_03, 'net_NTT2_D6':net_NTT2_D6, 'net_NTT2_D6_06':net_NTT2_D6_06, 'net_NTT2_D7_01':net_NTT2_D7_01, 
    'net_NTT2_D7_02':net_NTT2_D7_02, 'net_NTT2_D7_03':net_NTT2_D7_03, 'net_NTT2_E2':net_NTT2_E2, 'net_NTT2_E3':net_NTT2_E3, 'net_NTT2_F3A':net_NTT2_F3A, 'net_NTT2_F3B':net_NTT2_F3B, 'net_NTT2_F3D':net_NTT2_F3D, 
    'net_NTT2_F3E':net_NTT2_F3E, 'net_NTT2_G2':net_NTT2_G2, 'net_NTT2_G4':net_NTT2_G4, 'net_NTT3_A':net_NTT3_A, 'net_NTT3_B5':net_NTT3_B5, 'net_NTT3_C':net_NTT3_C, 'net_NTT3_D2':net_NTT3_D2, 'net_NTT3_D3':net_NTT3_D3, 
    'net_NTT3_D4':net_NTT3_D4, 'net_NTT3_D5':net_NTT3_D5, 'net_NTT5_A01':net_NTT5_A01, 'net_NTT5_B02':net_NTT5_B02, 'net_NTT5_B06':net_NTT5_B06, 'net_NTT5_C01':net_NTT5_C01, 'net_NTT5_D01':net_NTT5_D01, 
    'net_NTT5_D02A':net_NTT5_D02A, 'net_NTT5_D02B':net_NTT5_D02B, 'net_NTT5_E03':net_NTT5_E03, 'net_NTT5_E04':net_NTT5_E04, 'net_NTT5_F01':net_NTT5_F01, 'net_NTT5_F02':net_NTT5_F02, 'net_NTT5_F03':net_NTT5_F03, 
    'net_NTT5_G':net_NTT5_G, 'net_NTT5_G01':net_NTT5_G01, 'net_NTT5_G02':net_NTT5_G02, 'net_NTT5_G03':net_NTT5_G03, 'net_NTT5_H01':net_NTT5_H01, 'net_NTT5_H03':net_NTT5_H03, 'net_NTT5_I01':net_NTT5_I01, 
    'net_NTT5_I03':net_NTT5_I03, 'net_NTT5_J01':net_NTT5_J01, 'net_NTT5_J03':net_NTT5_J03, 'net_OP12_A':net_OP12_A, 'net_OP20_F1':net_OP20_F1, 'net_SG02_O':net_SG02_O, 'net_SG02_P':net_SG02_P, 'net_SG02_Q':net_SG02_Q, 
    'net_SG02_R':net_SG02_R, 'net_SG02_U':net_SG02_U,'net_GEG02_F':net_GEG02_F, 'dis_GEG02_F':dis_GEG02_F, 'GEG02_F':GEG02_F, 'GEG04_B3':GEG04_B3, 'GRTM_C503':GRTM_C503, 'dis_GEG04_B3':dis_GEG04_B3, 'dis_GRTM_C503':dis_GRTM_C503,
    'net_GEG04_B3':net_GEG04_B3, 'net_GRTM_C503':net_GRTM_C503})
