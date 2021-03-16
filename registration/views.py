from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from openpyxl import Workbook
from django.urls import reverse_lazy
import datetime
from datetime import date, timedelta
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from .models import (
   	Registration,
    
)

from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Q
from . forms import (
    Registration_form,
    
)
from django.views.generic import (
                				CreateView,
                				ListView,
                				UpdateView,
                				DetailView,
                				)
from bootstrap_modal_forms.generic import (
                                           BSModalDeleteView
                                           )

from .serializers import (
    RegistrationSerializer
    )

def registration_new(request):
    return render(request, 'registration_form.html')


# class regUpdate(SuccessMessageMixin, UpdateView):
# 	model = Registration
# 	form_class = reg_update_Form
# 	template_name = 'regupdate.html'
# 	success_url = reverse_lazy('registration_jan_reg')
# 	def get_success_message(self, cleaned_data):
# 		print(cleaned_data)
# 		return "Registrations Updated Successfully!"

def regUpdate(request, pk):
    if request.method == 'POST':
        PLATE_NO = request.POST.get('plate_no')
        CS_NO = request.POST.get('cs')
        CR_NAME = request.POST.get('cr_name')
        MODEL = request.POST.get('model')
        BRAND = request.POST.get('brand')
        VEHICLE_MAKE = request.POST.get('vmake')
        ENGINE_NO = request.POST.get('eng_no')
        CHASSIS_NO = request.POST.get('chassis_no')
        MV_FILE_NO = request.POST.get('mvfile')
        COC = request.POST.get('coc')
        SMOKE_TPL = request.POST.get('smoke')
        REMARKS_REGISTERED = request.POST.get('remarks_registered')
        DATE_EMAILED = request.POST.get('demail')
        JUSTIFICATION_REMARKS = request.POST.get('remarks_justification')

        reg = ''
        endplate = ''
        if PLATE_NO != '':
            endplate = int(PLATE_NO[-1])
            if endplate == 1:
                reg = 'JAN'
            elif endplate == 2:
                reg = 'FEB'
            elif endplate == 3:
                reg = 'MAR'
            elif endplate == 4:
                reg = 'APR'
            elif endplate == 5:
                reg = 'MAY'
            elif endplate == 6:
                reg = 'JUN'
            elif endplate == 7:
                reg = 'JUL'
            elif endplate == 8:
                reg = 'AUG'
            elif endplate == 9:
                reg = 'SEP'
            elif endplate == 0:
                reg = 'OCT' 
	
    Registration.objects.filter(id=pk).update(PLATE_NO=PLATE_NO,CS_NO=CS_NO,CR_NAME=CR_NAME,MODEL=MODEL,BRAND=BRAND,VEHICLE_MAKE=VEHICLE_MAKE,ENGINE_NO=ENGINE_NO,CHASSIS_NO=CHASSIS_NO,MV_FILE_NO=MV_FILE_NO,COC=COC,SMOKE_TPL=SMOKE_TPL,REMARKS_REGISTERED=REMARKS_REGISTERED,DATE_EMAILED=DATE_EMAILED,JUSTIFICATION_REMARKS=JUSTIFICATION_REMARKS,Registration_month=reg)
    return HttpResponseRedirect('/Registration/Details/{}'.format(pk))


class registrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all().order_by('id')
    serializer_class = RegistrationSerializer


def registrationCreate(request):
    if request.method == 'POST':
        PLATE_NO = request.POST.get('plate_no')
        CS_NO = request.POST.get('cs')
        CR_NAME = request.POST.get('cr_name')
        MODEL = request.POST.get('model')
        BRAND = request.POST.get('brand')
        VEHICLE_MAKE = request.POST.get('vmake')
        ENGINE_NO = request.POST.get('eng_no')
        CHASSIS_NO = request.POST.get('chassis_no')
        MV_FILE_NO = request.POST.get('mvfile')
        COC = request.POST.get('coc')
        SMOKE_TPL = request.POST.get('smoke')
        REMARKS_REGISTERED = request.POST.get('remarks_registered')
        DATE_EMAILED = request.POST.get('demail')
        JUSTIFICATION_REMARKS = request.POST.get('remarks_justification')

        reg = ''
        endplate = ''
        if PLATE_NO != '':
            endplate = int(PLATE_NO[-1])
            if endplate == 1:
                reg = 'JAN'
            elif endplate == 2:
                reg = 'FEB'
            elif endplate == 3:
                reg = 'MAR'
            elif endplate == 4:
                reg = 'APR'
            elif endplate == 5:
                reg = 'MAY'
            elif endplate == 6:
                reg = 'JUN'
            elif endplate == 7:
                reg = 'JUL'
            elif endplate == 8:
                reg = 'AUG'
            elif endplate == 9:
                reg = 'SEP'
            elif endplate == 0:
                reg = 'OCT' 

        saveto_end = Registration(PLATE_NO=PLATE_NO,CS_NO=CS_NO,CR_NAME=CR_NAME,MODEL=MODEL,BRAND=BRAND,
            VEHICLE_MAKE=VEHICLE_MAKE,ENGINE_NO=ENGINE_NO,CHASSIS_NO=CHASSIS_NO,MV_FILE_NO=MV_FILE_NO,
            COC=COC,SMOKE_TPL=SMOKE_TPL,REMARKS_REGISTERED=REMARKS_REGISTERED,DATE_EMAILED=DATE_EMAILED,
            JUSTIFICATION_REMARKS=JUSTIFICATION_REMARKS,Registration_month = reg,
            )
        saveto_end.save()

    return HttpResponseRedirect('/Registration/January')

class registrationDetails(DetailView):
    model = Registration
    template_name = 'registration_details.html'

# class registrationUpdate(UpdateView):
#     model = Registration
#     form_class = Vmasterlist
#     template_name = 'registration_form.html'

class registrationDeleteView(BSModalDeleteView):
    model = Registration
    template_name = 'registration_delete.html'
    success_message = 'Success: Item was deleted.'
    success_url = reverse_lazy('vehicle-list')


def othersRegView(request):
    context = {
            'others_list': Registration.objects.filter(PLATE_NO__contains="")
        }

    return render(request, 'reg_others.html', context)

def trailerRegView(request):
    context = {
            'trailer_list': Registration.objects.filter(BRAND__contains="TRAILER")
        }

    return render(request, 'reg_trailer.html', context)


def janRegView(request):
    context = {
            'jan_list': Registration.objects.filter(Registration_month__contains="JAN")
        }

    return render(request, 'regJan_monitoring.html', context)

def febRegView(request):
    context = {
            'feb_list': Registration.objects.filter(Registration_month__contains="FEB")
        }

    return render(request, 'regFeb_monitoring.html', context)

def marRegView(request):
    context = {
            'mar_list': Registration.objects.filter(Registration_month__contains="MAR")
        }

    return render(request, 'regMar_monitoring.html', context)

def aprRegView(request):
    context = {
            'apr_list': Registration.objects.filter(Registration_month__contains="APR")

        }

    return render(request, 'regApr_monitoring.html', context)

def mayRegView(request):
    context = {
            'may_list': Registration.objects.filter(Registration_month__contains="MAY")
        }

    return render(request, 'regMay_monitoring.html', context)

def junRegView(request):
    context = {
            'jun_list': Registration.objects.filter(Registration_month__contains="JUN")
        }

    return render(request, 'regJun_monitoring.html', context)

def julRegView(request):
    context = {
            'jul_list': Registration.objects.filter(Registration_month__contains="JUL")
        }
    return render(request, 'regJul_monitoring.html', context)

def augRegView(request):
    context = {
            'aug_list': Registration.objects.filter(Registration_month__contains="AUG")
        }

    return render(request, 'regAug_monitoring.html', context)

def sepRegView(request):
    context = {
            'sep_list': Registration.objects.filter(Registration_month__contains="SEP")
        }

    return render(request, 'regSep_monitoring.html', context)

def octRegView(request):
    context = {
            'oct_list': Registration.objects.filter(Registration_month__contains="OCT")
        }

    return render(request, 'regOct_monitoring.html', context)
