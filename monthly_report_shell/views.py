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
    shell_report_Serializer
    )
from . models import shell_report
from rest_framework import viewsets
from django.views.generic import (
                				CreateView,
                				ListView,
                				UpdateView,
                				DetailView,
                                DeleteView,
                				)
from django.db.models import Sum
from . forms import shell_form

from bootstrap_modal_forms.generic import BSModalDeleteView
                                           
def monthly_report_shell(request):
	return render(request, 'shell/shell_list.html')

class shell_report_ViewSet(viewsets.ModelViewSet):
    queryset = shell_report.objects.all().order_by('id')
    serializer_class = shell_report_Serializer

class shell_create(CreateView):
    model = shell_report
    form_class = shell_form
    template_name = 'shell/shell_create.html'

class shell_update(UpdateView):
    model = shell_report
    form_class = shell_form
    template_name = 'shell/shell_create.html'

# class shell_delete(BSModalDeleteView):
#     model = shell_report
#     template_name = 'shell/shell_delete.html'
#     success_message = 'Success: Item was deleted.'
    success_url = reverse_lazy('report_shell_list')
class shell_delete(DeleteView):
    model = shell_report
    success_url = reverse_lazy('report_shell_list')
    template_name = 'shell/shell_delete.html'

class shell_details(DetailView):
    model = shell_report
    template_name = 'shell/shell_detail.html'

def monthly_report_shellDetails(request):
    date = datetime.datetime.today()
    BB14_B10 = shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B10").aggregate(Sum('DelcoGrossValue'))
    BB14_B2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B2").aggregate(Sum('DelcoGrossValue'))
    BB14_B3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B3").aggregate(Sum('DelcoGrossValue'))
    BB14_B4=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B4").aggregate(Sum('DelcoGrossValue'))
    BB14_B5=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B5").aggregate(Sum('DelcoGrossValue'))
    BB14_B6=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B6").aggregate(Sum('DelcoGrossValue'))
    BB14_B7=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B7").aggregate(Sum('DelcoGrossValue'))
    BB14_B8=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B8").aggregate(Sum('DelcoGrossValue'))
    BB14_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-E").aggregate(Sum('DelcoGrossValue'))
    CMB4_B=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMB4-B").aggregate(Sum('DelcoGrossValue'))
    CMG12_D=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG12-D").aggregate(Sum('DelcoGrossValue'))
    CMG2_B1=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-B1").aggregate(Sum('DelcoGrossValue'))
    CMG2_B3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-B3").aggregate(Sum('DelcoGrossValue'))
    CMG2_C1=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C1").aggregate(Sum('DelcoGrossValue'))
    CMG2_C2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C2").aggregate(Sum('DelcoGrossValue'))
    CMG2_C3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C3").aggregate(Sum('DelcoGrossValue'))
    CMG2_C4=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C4").aggregate(Sum('DelcoGrossValue'))
    CMG2_C5_B=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C5-B").aggregate(Sum('DelcoGrossValue'))
    CMG2_C5_C=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C5-C").aggregate(Sum('DelcoGrossValue'))
    CMG2_C5_G=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C5-G").aggregate(Sum('DelcoGrossValue'))
    CMG2_D1=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-D1").aggregate(Sum('DelcoGrossValue'))
    CMG2_D2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-D2").aggregate(Sum('DelcoGrossValue'))
    CMG2_D3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-D3").aggregate(Sum('DelcoGrossValue'))
    CMG2_E2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-E2").aggregate(Sum('DelcoGrossValue'))
    CMG2_E3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-E3").aggregate(Sum('DelcoGrossValue'))
    CMG2_F1=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-F1").aggregate(Sum('DelcoGrossValue'))
    CMG2_F2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-F2").aggregate(Sum('DelcoGrossValue'))
    CMG2_F3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-F3").aggregate(Sum('DelcoGrossValue'))
    CMG3_A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG3-A").aggregate(Sum('DelcoGrossValue'))
    CMG4_B=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG4-B").aggregate(Sum('DelcoGrossValue'))
    CMG4_C=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG4-C").aggregate(Sum('DelcoGrossValue'))
    CMG4_D=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG4-D").aggregate(Sum('DelcoGrossValue'))
    CMG4_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG4-E").aggregate(Sum('DelcoGrossValue'))
    CMG4_F=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG4-F").aggregate(Sum('DelcoGrossValue'))
    CMG4_G=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG4-G").aggregate(Sum('DelcoGrossValue'))
    CMG5_D=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG5-D").aggregate(Sum('DelcoGrossValue'))
    CMG5_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG5-E").aggregate(Sum('DelcoGrossValue'))
    CMG5_G=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG5-G").aggregate(Sum('DelcoGrossValue'))
    CMG6_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG6-E").aggregate(Sum('DelcoGrossValue'))
    CRA6_A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CRA6-A").aggregate(Sum('DelcoGrossValue'))
    EIG09_A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="EIG09-A").aggregate(Sum('DelcoGrossValue'))
    FIN13_K1=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN13-K1").aggregate(Sum('DelcoGrossValue'))
    FIN13_K2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN13-K2").aggregate(Sum('DelcoGrossValue'))
    FIN22_D1b=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN22-D1b").aggregate(Sum('DelcoGrossValue'))
    FIN22_D2a=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN22-D2a").aggregate(Sum('DelcoGrossValue'))
    FIN23_C1 =shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN23-C1").aggregate(Sum('DelcoGrossValue'))
    FIN9_C0301=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN9-C0301").aggregate(Sum('DelcoGrossValue'))
    FIN9_E02=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN9-E02").aggregate(Sum('DelcoGrossValue'))
    FIN9_F0201=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN9-F0201").aggregate(Sum('DelcoGrossValue'))
    FIN_F0201=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN-F0201").aggregate(Sum('DelcoGrossValue'))
    GEG02_A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-A").aggregate(Sum('DelcoGrossValue'))
    GEG02_B=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-B").aggregate(Sum('DelcoGrossValue'))
    GEG02_C=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-C").aggregate(Sum('DelcoGrossValue'))
    GEG02_D=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-D").aggregate(Sum('DelcoGrossValue'))
    GEG02_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-E").aggregate(Sum('DelcoGrossValue'))
    GEG02_F=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-F").aggregate(Sum('DelcoGrossValue'))
    GEG02_G=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-G").aggregate(Sum('DelcoGrossValue'))
    GEG02_H=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-H").aggregate(Sum('DelcoGrossValue'))
    GEG02_K =shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-K").aggregate(Sum('DelcoGrossValue'))
    GEG04_B=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG04-B").aggregate(Sum('DelcoGrossValue'))
    GENT_F2011=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GENT-F2011").aggregate(Sum('DelcoGrossValue'))
    NTT2_D06_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-D06-E").aggregate(Sum('DelcoGrossValue'))
    NTT2_D5_03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-D5-03").aggregate(Sum('DelcoGrossValue'))
    NTT2_D5_05=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-D5-05").aggregate(Sum('DelcoGrossValue'))
    NTT2_D6_03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-D6-03").aggregate(Sum('DelcoGrossValue'))
    NTT2_D6_05=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-D6-05").aggregate(Sum('DelcoGrossValue'))
    NTT2_F4=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-F4").aggregate(Sum('DelcoGrossValue'))
    NTT2_G4=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-G4").aggregate(Sum('DelcoGrossValue'))
    NTT2_H3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-H3").aggregate(Sum('DelcoGrossValue'))
    NTT3_B5=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT3-B5").aggregate(Sum('DelcoGrossValue'))
    NTT3_D5=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT3-D5").aggregate(Sum('DelcoGrossValue'))
    NTT5_B05A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-B05A").aggregate(Sum('DelcoGrossValue'))
    NTT5_B06=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-B06").aggregate(Sum('DelcoGrossValue'))
    NTT5_C01 =shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-C01").aggregate(Sum('DelcoGrossValue'))
    NTT5_D01=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-D01").aggregate(Sum('DelcoGrossValue'))
    NTT5_D02=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-D02").aggregate(Sum('DelcoGrossValue'))
    NTT5_E03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-E03").aggregate(Sum('DelcoGrossValue'))
    NTT5_E04=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-E04").aggregate(Sum('DelcoGrossValue'))
    NTT5_G01=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-G01").aggregate(Sum('DelcoGrossValue'))
    NTT5_G02=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-G02").aggregate(Sum('DelcoGrossValue'))
    NTT5_G03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-G03").aggregate(Sum('DelcoGrossValue'))
    NTT5_H01=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-H01").aggregate(Sum('DelcoGrossValue'))
    NTT5_H03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-H03").aggregate(Sum('DelcoGrossValue'))
    NTT5_I01=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-I01").aggregate(Sum('DelcoGrossValue'))
    NTT5_I02=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-I02").aggregate(Sum('DelcoGrossValue'))
    NTT5_I03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-I03").aggregate(Sum('DelcoGrossValue'))
    NTT5_J01=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-J01").aggregate(Sum('DelcoGrossValue'))
    NTT5_J02=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-J02").aggregate(Sum('DelcoGrossValue'))
    NTT5_J03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-J03").aggregate(Sum('DelcoGrossValue'))
    NTT6_C=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT6-C").aggregate(Sum('DelcoGrossValue'))
    NTT7_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT7-E").aggregate(Sum('DelcoGrossValue'))
    OP12_A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="OP12-A").aggregate(Sum('DelcoGrossValue'))
    SG02_O=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-O").aggregate(Sum('DelcoGrossValue'))
    SG02_O2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-O2").aggregate(Sum('DelcoGrossValue'))
    SG02_P=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-P").aggregate(Sum('DelcoGrossValue'))
    SG02_Q=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-Q").aggregate(Sum('DelcoGrossValue'))
    SG02_Q2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-Q2").aggregate(Sum('DelcoGrossValue'))
    SG02_R=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-R").aggregate(Sum('DelcoGrossValue'))
    SG02_U=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-U").aggregate(Sum('DelcoGrossValue'))
    SG11_A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG11-A").aggregate(Sum('DelcoGrossValue'))
    ST1=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="ST1").aggregate(Sum('DelcoGrossValue'))
    

    rebate_BB14_B10 = shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B10").aggregate(Sum('RebateCustAmount'))
    rebate_BB14_B2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B2").aggregate(Sum('RebateCustAmount'))
    rebate_BB14_B3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B3").aggregate(Sum('RebateCustAmount'))
    rebate_BB14_B4=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B4").aggregate(Sum('RebateCustAmount'))
    rebate_BB14_B5=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B5").aggregate(Sum('RebateCustAmount'))
    rebate_BB14_B6=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B6").aggregate(Sum('RebateCustAmount'))
    rebate_BB14_B7=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B7").aggregate(Sum('RebateCustAmount'))
    rebate_BB14_B8=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-B8").aggregate(Sum('RebateCustAmount'))
    rebate_BB14_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="BB14-E").aggregate(Sum('RebateCustAmount'))
    rebate_CMB4_B=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMB4-B").aggregate(Sum('RebateCustAmount'))
    rebate_CMG12_D=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG12-D").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_B1=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-B1").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_B3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-B3").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_C1=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C1").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_C2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C2").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_C3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C3").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_C4=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C4").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_C5_B=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C5-B").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_C5_C=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C5-C").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_C5_G=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-C5-G").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_D1=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-D1").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_D2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-D2").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_D3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-D3").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_E2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-E2").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_E3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-E3").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_F1=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-F1").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_F2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-F2").aggregate(Sum('RebateCustAmount'))
    rebate_CMG2_F3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG2-F3").aggregate(Sum('RebateCustAmount'))
    rebate_CMG3_A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG3-A").aggregate(Sum('RebateCustAmount'))
    rebate_CMG4_B=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG4-B").aggregate(Sum('RebateCustAmount'))
    rebate_CMG4_C=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG4-C").aggregate(Sum('RebateCustAmount'))
    rebate_CMG4_D=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG4-D").aggregate(Sum('RebateCustAmount'))
    rebate_CMG4_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG4-E").aggregate(Sum('RebateCustAmount'))
    rebate_CMG4_F=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG4-F").aggregate(Sum('RebateCustAmount'))
    rebate_CMG4_G=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG4-G").aggregate(Sum('RebateCustAmount'))
    rebate_CMG5_D=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG5-D").aggregate(Sum('RebateCustAmount'))
    rebate_CMG5_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG5-E").aggregate(Sum('RebateCustAmount'))
    rebate_CMG5_G=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG5-G").aggregate(Sum('RebateCustAmount'))
    rebate_CMG6_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CMG6-E").aggregate(Sum('RebateCustAmount'))
    rebate_CRA6_A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="CRA6-A").aggregate(Sum('RebateCustAmount'))
    rebate_EIG09_A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="EIG09-A").aggregate(Sum('RebateCustAmount'))
    rebate_FIN13_K1=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN13-K1").aggregate(Sum('RebateCustAmount'))
    rebate_FIN13_K2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN13-K2").aggregate(Sum('RebateCustAmount'))
    rebate_FIN22_D1b=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN22-D1b").aggregate(Sum('RebateCustAmount'))
    rebate_FIN22_D2a=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN22-D2a").aggregate(Sum('RebateCustAmount'))
    rebate_FIN23_C1 =shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN23-C1").aggregate(Sum('RebateCustAmount'))
    rebate_FIN9_C0301=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN9-C0301").aggregate(Sum('RebateCustAmount'))
    rebate_FIN9_E02=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN9-E02").aggregate(Sum('RebateCustAmount'))
    rebate_FIN9_F0201=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN9-F0201").aggregate(Sum('RebateCustAmount'))
    rebate_FIN_F0201=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="FIN-F0201").aggregate(Sum('RebateCustAmount'))
    rebate_GEG02_A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-A").aggregate(Sum('RebateCustAmount'))
    rebate_GEG02_B=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-B").aggregate(Sum('RebateCustAmount'))
    rebate_GEG02_C=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-C").aggregate(Sum('RebateCustAmount'))
    rebate_GEG02_D=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-D").aggregate(Sum('RebateCustAmount'))
    rebate_GEG02_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-E").aggregate(Sum('RebateCustAmount'))
    rebate_GEG02_F=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-F").aggregate(Sum('RebateCustAmount'))
    rebate_GEG02_G=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-G").aggregate(Sum('RebateCustAmount'))
    rebate_GEG02_H=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-H").aggregate(Sum('RebateCustAmount'))
    rebate_GEG02_K =shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG02-K").aggregate(Sum('RebateCustAmount'))
    rebate_GEG04_B=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GEG04-B").aggregate(Sum('RebateCustAmount'))
    rebate_GENT_F2011=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="GENT-F2011").aggregate(Sum('RebateCustAmount'))
    rebate_NTT2_D06_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-D06-E").aggregate(Sum('RebateCustAmount'))
    rebate_NTT2_D5_03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-D5-03").aggregate(Sum('RebateCustAmount'))
    rebate_NTT2_D5_05=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-D5-05").aggregate(Sum('RebateCustAmount'))
    rebate_NTT2_D6_03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-D6-03").aggregate(Sum('RebateCustAmount'))
    rebate_NTT2_D6_05=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-D6-05").aggregate(Sum('RebateCustAmount'))
    rebate_NTT2_F4=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-F4").aggregate(Sum('RebateCustAmount'))
    rebate_NTT2_G4=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-G4").aggregate(Sum('RebateCustAmount'))
    rebate_NTT2_H3=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT2-H3").aggregate(Sum('RebateCustAmount'))
    rebate_NTT3_B5=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT3-B5").aggregate(Sum('RebateCustAmount'))
    rebate_NTT3_D5=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT3-D5").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_B05A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-B05A").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_B06=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-B06").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_C01 =shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-C01").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_D01=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-D01").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_D02=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-D02").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_E03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-E03").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_E04=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-E04").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_G01=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-G01").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_G02=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-G02").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_G03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-G03").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_H01=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-H01").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_H03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-H03").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_I01=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-I01").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_I02=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-I02").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_I03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-I03").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_J01=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-J01").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_J02=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-J02").aggregate(Sum('RebateCustAmount'))
    rebate_NTT5_J03=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT5-J03").aggregate(Sum('RebateCustAmount'))
    rebate_NTT6_C=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT6-C").aggregate(Sum('RebateCustAmount'))
    rebate_NTT7_E=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="NTT7-E").aggregate(Sum('RebateCustAmount'))
    rebate_OP12_A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="OP12-A").aggregate(Sum('RebateCustAmount'))
    rebate_SG02_O=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-O").aggregate(Sum('RebateCustAmount'))
    rebate_SG02_O2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-O2").aggregate(Sum('RebateCustAmount'))
    rebate_SG02_P=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-P").aggregate(Sum('RebateCustAmount'))
    rebate_SG02_Q=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-Q").aggregate(Sum('RebateCustAmount'))
    rebate_SG02_Q2=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-Q2").aggregate(Sum('RebateCustAmount'))
    rebate_SG02_R=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-R").aggregate(Sum('RebateCustAmount'))
    rebate_SG02_U=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG02-U").aggregate(Sum('RebateCustAmount'))
    rebate_SG11_A=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="SG11-A").aggregate(Sum('RebateCustAmount'))
    rebate_ST1=shell_report.objects.filter(InvoiceDate__year=date.year, 
        InvoiceDate__month=date.month, Supplier='Shell', CostCenter="ST1").aggregate(Sum('RebateCustAmount'))
    
    
    return render(request, 'shell/shell_summary.html',{'title' : 'Shell Report', 'BB14_B10':BB14_B10,'BB14_B2':BB14_B2,'BB14_B3':BB14_B3,'BB14_B4':BB14_B4,'BB14_B5':BB14_B5,'BB14_B6':BB14_B6,'BB14_B7':BB14_B7,'BB14_B8':BB14_B8,'BB14_E':BB14_E,'CMB4_B':CMB4_B,'CMG12_D':CMG12_D,'CMG2_B1':CMG2_B1,
    'CMG2_B3':CMG2_B3,'CMG2_C1':CMG2_C1,'CMG2_C2':CMG2_C2,'CMG2_C3':CMG2_C3,'CMG2_C4':CMG2_C4,'CMG2_C5_B':CMG2_C5_B,'CMG2_C5_C':CMG2_C5_C,'CMG2_C5_G':CMG2_C5_G,'CMG2_D1':CMG2_D1,'CMG2_D2':CMG2_D2,'CMG2_D3':CMG2_D3,
    'CMG2_E2':CMG2_E2,'CMG2_E3':CMG2_E3,'CMG2_F1':CMG2_F1,'CMG2_F2':CMG2_F2,'CMG2_F3':CMG2_F3,'CMG3_A':CMG3_A,'CMG4_B':CMG4_B,'CMG4_C':CMG4_C,'CMG4_D':CMG4_D,'CMG4_E':CMG4_E,'CMG4_F':CMG4_F,'CMG4_G':CMG4_G,'CMG5_D':CMG5_D,
    'CMG5_E':CMG5_E,'CMG5_G':CMG5_G,'CMG6_E':CMG6_E,'CRA6_A':CRA6_A,'EIG09_A':EIG09_A,'FIN13_K1':FIN13_K1,'FIN13_K2':FIN13_K2,'FIN22_D1b':FIN22_D1b,'FIN22_D2a':FIN22_D2a,'FIN23_C1':FIN23_C1 ,
    'FIN9_C0301':FIN9_C0301,'FIN9_E02':FIN9_E02,'FIN9_F0201':FIN9_F0201,'FIN_F0201':FIN_F0201,'GEG02_A':GEG02_A,'GEG02_B':GEG02_B,'GEG02_C':GEG02_C,'GEG02_D':GEG02_D,'GEG02_E':GEG02_E,
    'GEG02_F':GEG02_F,'GEG02_G':GEG02_G,'GEG02_H':GEG02_H,'GEG02_K':GEG02_K ,'GEG04_B':GEG04_B,'GENT_F2011':GENT_F2011,'NTT2_D06_E':NTT2_D06_E,'NTT2_D5_03':NTT2_D5_03,'NTT2_D5_05':NTT2_D5_05,'NTT2_D6_03':NTT2_D6_03,
    'NTT2_D6_05':NTT2_D6_05,'NTT2_F4':NTT2_F4,'NTT2_G4':NTT2_G4,'NTT2_H3':NTT2_H3,'NTT3_B5':NTT3_B5,'NTT3_D5':NTT3_D5,'NTT5_B05A':NTT5_B05A,'NTT5_B06':NTT5_B06,'NTT5_C01':NTT5_C01 ,'NTT5_D01':NTT5_D01,'NTT5_D02':NTT5_D02,
    'NTT5_E03':NTT5_E03,'NTT5_E04':NTT5_E04,'NTT5_G01':NTT5_G01,'NTT5_G02':NTT5_G02,'NTT5_G03':NTT5_G03,'NTT5_H01':NTT5_H01,'NTT5_H03':NTT5_H03,'NTT5_I01':NTT5_I01,'NTT5_I02':NTT5_I02,'NTT5_I03':NTT5_I03,'NTT5_J01':NTT5_J01,
    'NTT5_J02':NTT5_J02,'NTT5_J03':NTT5_J03,'NTT6_C':NTT6_C,'NTT7_E':NTT7_E,'OP12_A':OP12_A,'SG02_O':SG02_O,'SG02_O2':SG02_O2,'SG02_P':SG02_P,'SG02_Q':SG02_Q,'SG02_Q2':SG02_Q2,'SG02_R':SG02_R,'SG02_U':SG02_U,'SG11_A':SG11_A,'ST1':ST1,
    'rebate_BB14_B10':rebate_BB14_B10,'rebate_BB14_B2':rebate_BB14_B2,'rebate_BB14_B3':rebate_BB14_B3,'rebate_BB14_B4':rebate_BB14_B4,'rebate_BB14_B5':rebate_BB14_B5,'rebate_BB14_B6':rebate_BB14_B6,'rebate_BB14_B7':rebate_BB14_B7,'rebate_BB14_B8':rebate_BB14_B8,'rebate_BB14_E':rebate_BB14_E,'rebate_CMB4_B':rebate_CMB4_B,'rebate_CMG12_D':rebate_CMG12_D,'rebate_CMG2_B1':rebate_CMG2_B1,
    'rebate_CMG2_B3':rebate_CMG2_B3,'rebate_CMG2_C1':rebate_CMG2_C1,'rebate_CMG2_C2':rebate_CMG2_C2,'rebate_CMG2_C3':rebate_CMG2_C3,'rebate_CMG2_C4':rebate_CMG2_C4,'rebate_CMG2_C5_B':rebate_CMG2_C5_B,'rebate_CMG2_C5_C':rebate_CMG2_C5_C,'rebate_CMG2_C5_G':rebate_CMG2_C5_G,'rebate_CMG2_D1':rebate_CMG2_D1,'rebate_CMG2_D2':rebate_CMG2_D2,'rebate_CMG2_D3':rebate_CMG2_D3,
    'rebate_CMG2_E2':rebate_CMG2_E2,'rebate_CMG2_E3':rebate_CMG2_E3,'rebate_CMG2_F1':rebate_CMG2_F1,'rebate_CMG2_F2':rebate_CMG2_F2,'rebate_CMG2_F3':rebate_CMG2_F3,'rebate_CMG3_A':rebate_CMG3_A,'rebate_CMG4_B':rebate_CMG4_B,'rebate_CMG4_C':rebate_CMG4_C,'rebate_CMG4_D':rebate_CMG4_D,'rebate_CMG4_E':rebate_CMG4_E,'rebate_CMG4_F':rebate_CMG4_F,'rebate_CMG4_G':rebate_CMG4_G,'rebate_CMG5_D':rebate_CMG5_D,
    'rebate_CMG5_E':rebate_CMG5_E,'rebate_CMG5_G':rebate_CMG5_G,'rebate_CMG6_E':rebate_CMG6_E,'rebate_CRA6_A':rebate_CRA6_A,'rebate_EIG09_A':rebate_EIG09_A,'rebate_FIN13_K1':rebate_FIN13_K1,'rebate_FIN13_K2':rebate_FIN13_K2,'rebate_FIN22_D1b':rebate_FIN22_D1b,'rebate_FIN22_D2a':rebate_FIN22_D2a,'rebate_FIN23_C1':rebate_FIN23_C1 ,
    'rebate_FIN9_C0301':rebate_FIN9_C0301,'rebate_FIN9_E02':rebate_FIN9_E02,'rebate_FIN9_F0201':rebate_FIN9_F0201,'rebate_FIN_F0201':rebate_FIN_F0201,'rebate_GEG02_A':rebate_GEG02_A,'rebate_GEG02_B':rebate_GEG02_B,'rebate_GEG02_C':rebate_GEG02_C,'rebate_GEG02_D':rebate_GEG02_D,'rebate_GEG02_E':rebate_GEG02_E,
    'rebate_GEG02_F':rebate_GEG02_F,'rebate_GEG02_G':rebate_GEG02_G,'rebate_GEG02_H':rebate_GEG02_H,'rebate_GEG02_K':rebate_GEG02_K ,'rebate_GEG04_B':rebate_GEG04_B,'rebate_GENT_F2011':rebate_GENT_F2011,'rebate_NTT2_D06_E':rebate_NTT2_D06_E,'rebate_NTT2_D5_03':rebate_NTT2_D5_03,'rebate_NTT2_D5_05':rebate_NTT2_D5_05,'rebate_NTT2_D6_03':rebate_NTT2_D6_03,
    'rebate_NTT2_D6_05':rebate_NTT2_D6_05,'rebate_NTT2_F4':rebate_NTT2_F4,'rebate_NTT2_G4':rebate_NTT2_G4,'rebate_NTT2_H3':rebate_NTT2_H3,'rebate_NTT3_B5':rebate_NTT3_B5,'rebate_NTT3_D5':rebate_NTT3_D5,'rebate_NTT5_B05A':rebate_NTT5_B05A,'rebate_NTT5_B06':rebate_NTT5_B06,'rebate_NTT5_C01':rebate_NTT5_C01 ,'rebate_NTT5_D01':rebate_NTT5_D01,'rebate_NTT5_D02':rebate_NTT5_D02,
    'rebate_NTT5_E03':rebate_NTT5_E03,'rebate_NTT5_E04':rebate_NTT5_E04,'rebate_NTT5_G01':rebate_NTT5_G01,'rebate_NTT5_G02':rebate_NTT5_G02,'rebate_NTT5_G03':rebate_NTT5_G03,'rebate_NTT5_H01':rebate_NTT5_H01,'rebate_NTT5_H03':rebate_NTT5_H03,'rebate_NTT5_I01':rebate_NTT5_I01,'rebate_NTT5_I02':rebate_NTT5_I02,'rebate_NTT5_I03':rebate_NTT5_I03,'rebate_NTT5_J01':rebate_NTT5_J01,
    'rebate_NTT5_J02':rebate_NTT5_J02,'rebate_NTT5_J03':rebate_NTT5_J03,'rebate_NTT6_C':rebate_NTT6_C,'rebate_NTT7_E':rebate_NTT7_E,'rebate_OP12_A':rebate_OP12_A,'rebate_SG02_O':rebate_SG02_O,'rebate_SG02_O2':rebate_SG02_O2,'rebate_SG02_P':rebate_SG02_P,'rebate_SG02_Q':rebate_SG02_Q,'rebate_SG02_Q2':rebate_SG02_Q2,'rebate_SG02_R':rebate_SG02_R,'rebate_SG02_U':rebate_SG02_U,'rebate_SG11_A':rebate_SG11_A,'rebate_ST1':rebate_ST1
    })

