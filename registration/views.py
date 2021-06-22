import os
import numpy as np
import pandas as pd
import datetime
from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .render import Render
from openpyxl import Workbook
from django.urls import reverse_lazy
from django.core.mail import get_connection,send_mail
from django.core import mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import Context
from datetime import date, timedelta
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from .models import (
   	Registration,
    CarRegistration
)
from django import template
register = template.Library()
from django.template.defaultfilters import floatformat
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
                                View,
                				)
from bootstrap_modal_forms.generic import (
                                           BSModalDeleteView
                                           )

from .serializers import (
    RegistrationSerializer
    )


def registration_new(request):
    return render(request, 'registration_form.html')

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
        email_status = request.POST.get('email_status')
        email = request.POST.get('email')

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
	
    Registration.objects.filter(id=pk).update(PLATE_NO=PLATE_NO, Plate_ending=endplate, CS_NO=CS_NO, CR_NAME=CR_NAME, MODEL=MODEL,BRAND=BRAND,VEHICLE_MAKE=VEHICLE_MAKE,ENGINE_NO=ENGINE_NO,CHASSIS_NO=CHASSIS_NO,MV_FILE_NO=MV_FILE_NO,COC=COC,SMOKE_TPL=SMOKE_TPL,REMARKS_REGISTERED=REMARKS_REGISTERED,DATE_EMAILED=DATE_EMAILED,JUSTIFICATION_REMARKS=JUSTIFICATION_REMARKS,Registration_month=reg, sent_email=email_status, email=email)
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
        email_status = request.POST.get('email_status')
        email = request.POST.get('email')

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

        saveto_end = Registration(PLATE_NO=PLATE_NO,Plate_ending= endplate, CS_NO=CS_NO, CR_NAME=CR_NAME, MODEL=MODEL,BRAND=BRAND,
            VEHICLE_MAKE=VEHICLE_MAKE, ENGINE_NO=ENGINE_NO, CHASSIS_NO=CHASSIS_NO, MV_FILE_NO=MV_FILE_NO,
            COC=COC, SMOKE_TPL=SMOKE_TPL, REMARKS_REGISTERED=REMARKS_REGISTERED, DATE_EMAILED=DATE_EMAILED,
            JUSTIFICATION_REMARKS=JUSTIFICATION_REMARKS, Registration_month = reg, sent_email=email_status, email=email
            )
        saveto_end.save()

    return HttpResponseRedirect('/Registration/January')

class registrationDetails(DetailView):
    model = Registration
    template_name = 'registration_details.html'


class registrationDeleteView(BSModalDeleteView):
    model = Registration
    template_name = 'registration_delete.html'
    success_message = 'Success: Item was deleted.'
    success_url = reverse_lazy('vehicle-list')


def othersRegView(request):
    context = {
            'other_list': Registration.objects.filter(PLATE_NO__isnull=True)
        }

    return render(request, 'reg_others.html', context)

def trailerRegView(request):
    context = {
            'trailer_list': Registration.objects.filter(BRAND__contains="TRAILER",PLATE_NO__isnull=True)
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

def summary(request):
        context = {
            'reg_report':Registration.objects.all()
        }
        return render(request, 'summaryV2.html', context)


class registrationsPDFView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    @register.filter
    def as_percentage_of(part, whole):
        try:
            return "%d%%" % (float(part) / whole * 100)
        except (ValueError, ZeroDivisionError):
            return ""
    def get(self, request, pk, *args, **kwargs):
        reg_report = Registration.objects.get(pk=pk)
        return Render.render('reg_summary_report.html', {'reg_report': reg_report})

def registration_excel(request):
    rental_queryset = Registration.objects.all()   
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=Registration.xlsx'
    workbook = Workbook()

    worksheet = workbook.active
    worksheet.title = 'Registration'

    columns = [
        'Plate No' ,
        'Plate Ending' ,
        'CS NO' ,
        'CR NAME' ,
        'MODEL' ,
        'BRAND' ,
        'VEHICLE MAKE' ,
        'ENGINE NO' ,
        'CHASSIS NO' ,
        'MV_FILE NO' ,
        'COC' ,
        'SMOKE TPL' ,
        'REMARKS REGISTERED' ,
        'DATE EMAILED' ,
        'JUSTIFICATION REMARKS' ,
        'Registration month' ,
        'Email' ,
        'Sent email' ,
        'Date email log' ,
    ]
    row_num = 1

    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title

    for car in rental_queryset:
        row_num += 1
        row = [
                car.PLATE_NO ,
                car.Plate_ending ,
                car.CS_NO ,
                car.CR_NAME ,
                car.MODEL ,
                car.BRAND ,
                car.VEHICLE_MAKE ,
                car.ENGINE_NO ,
                car.CHASSIS_NO ,
                car.MV_FILE_NO ,
                car.COC ,
                car.SMOKE_TPL ,
                car.REMARKS_REGISTERED ,
                car.DATE_EMAILED ,
                car.JUSTIFICATION_REMARKS ,
                car.Registration_month ,
                car.email ,
                car.sent_email ,
                car.Date_email_log ,
        ]
        
        for col_num, cell_value in enumerate(row, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = cell_value

    workbook.save(response)
    return response


class HomeView():
    month = datetime.datetime.now().month
    date_now = datetime.datetime.now().date()
    print(date_now)
    sent_status = Registration.objects.all()
    if month == 1:
        car_status = Registration.objects.filter(
            Registration_month="JAN", sent_email="No")
        plate = ""
        for carreg in car_status:
                # print(carreg.plate_no)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                subject = 'Fleet Management System Automated Email'
                html_message = render_to_string('email.html',{'content':item.PLATE_NO})
                plain_message = item.PLATE_NO
                recipient_list = [item.email]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 2:
        car_status = Registration.objects.filter(
            Registration_month="FEB", sent_email="No")
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                subject = 'Fleet Management System Automated Email'
                html_message = render_to_string('email.html',{'content':item.PLATE_NO})
                plain_message = item.PLATE_NO
                recipient_list = [item.email]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 3:
        car_status = Registration.objects.filter(
            Registration_month="MAR", sent_email="No")
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                subject = 'Fleet Management System Automated Email'
                html_message = render_to_string('email.html',{'content':item.PLATE_NO})
                plain_message = item.PLATE_NO
                recipient_list = [item.email]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 4:
        car_status = Registration.objects.filter(
            Registration_month="APR", sent_email="No")
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                subject = 'Fleet Management System Automated Email'
                html_message = render_to_string('email.html',{'content':item.PLATE_NO})
                plain_message = item.PLATE_NO
                recipient_list = [item.email]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 5:
        car_status = Registration.objects.filter(
            Registration_month="MAY", sent_email="No")
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                subject = 'Fleet Management System Automated Email'
                html_message = render_to_string('email.html',{'content':item.PLATE_NO})
                plain_message = item.PLATE_NO
                recipient_list = [item.email]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 6:
        car_status = Registration.objects.filter(
            Registration_month="JUN", sent_email="No")
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                subject = 'Fleet Management System Automated Email'
                html_message = render_to_string('email.html',{'content':item.PLATE_NO})
                plain_message = item.PLATE_NO
                recipient_list = [item.email]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 7:
        car_status = Registration.objects.filter(
            Registration_month="JUL", sent_email="No")
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                subject = 'Fleet Management System Automated Email'
                html_message = render_to_string('email.html',{'content':item.PLATE_NO})
                plain_message = item.PLATE_NO
                recipient_list = [item.email]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 8:
        car_status = Registration.objects.filter(
            Registration_month="AUG", sent_email="No")
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                subject = 'Fleet Management System Automated Email'
                html_message = render_to_string('email.html',{'content':item.PLATE_NO})
                plain_message = item.PLATE_NO
                recipient_list = [item.email]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 9:
        car_status = Registration.objects.filter(
            Registration_month="SEP", sent_email="No")
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                subject = 'Fleet Management System Automated Email'
                html_message = render_to_string('email.html',{'content':item.PLATE_NO})
                plain_message = item.PLATE_NO
                recipient_list = [item.email]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 0:
        car_status = Registration.objects.filter(
            Registration_month="OCT", sent_email="No")
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                subject = 'Fleet Management System Automated Email'
                html_message = render_to_string('email.html',{'content':item.PLATE_NO})
                plain_message = item.PLATE_NO
                recipient_list = [item.email]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    model = Registration
    context_object_name = 'car_list'
    template_name = 'account/account/base/login.html'

# Registration Daily Report
    
def registration_report(request):
    username = os.getlogin()
    today = datetime.datetime.now()
    month = today.month
    def excel_report(reg):
        Registration_due_1 = Registration.objects.filter(Plate_ending=month)
        Registration_total_1 = Registration.objects.filter(Plate_ending=month).count()
        if Registration_total_1 == 0:
            ws.append([reg, 0, ])
            ws['B7'].value = Registration_total_1
        else:
            for reg_due in Registration_due_1:
                ws.append([reg, ])
                ws['B7'].value = Registration_total_1
                break
            
    from openpyxl import Workbook, load_workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Registration Report"
    ws['A1'].value = "PERSONNEL:Francis Jae Dela Cruz"
    ws['A3'].value = "OUTPUT"
    ws['A4'].value = ""
    ws['A5'].value = ""
    ws.append(['', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Remarks'])

    excel_report("Due For Regs")
    excel_report("Registered")
    excel_report("unRegistered")
    excel_report("Uploading")
    excel_report("Alarm")
    excel_report("Completed")
    if month == 1:
        ws['A5'].value = "Ending 1"
    elif month == 2:
        ws['A5'].value = "Ending 2"
    elif month == 3:
        ws['A5'].value = "Ending 3"
    elif month == 4:
        ws['A5'].value = "Ending 4"
    elif month == 5:
        ws['A5'].value = "Ending 5"
    elif month == 6:
        ws['A5'].value = "Ending 6"
    elif month == 7:
        ws['A5'].value = "Ending 7"
    elif month == 8:
        ws['A5'].value = "Ending 8"
    elif month == 9:
        ws['A5'].value = "Ending 9"
    elif month == 10:
        ws['A5'].value = "Ending 0"
    # ws1 = wb.active
    # ws1['A15'].value = ""
    # ws1['A16'].value = "Ending 1"
    # ws1.append(['', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Remarks'])

    # excel_report("Due For Regs")
    # excel_report("Registered")
    # excel_report("unRegistered")
    # excel_report("Uploading")
    # excel_report("Alarm")
    # excel_report("Completed")

    # ws2 = wb.active
    # ws2['A26'].value = ""
    # ws2['A27'].value = "Ending 2"
    # ws2.append(['', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Remarks'])

    # excel_report("Due For Regs")
    # excel_report("Registered")
    # excel_report("unRegistered")
    # excel_report("Uploading")
    # excel_report("Alarm")
    # excel_report("Completed")

    # ws3 = wb.active
    # ws3.title = "Registration Report"
    # ws3['A36'].value = ""
    # ws3['A37'].value = "Ending 3"
    # ws3.append(['', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Remarks'])

    # excel_report("Due For Regs")
    # excel_report("Registered")
    # excel_report("unRegistered")
    # excel_report("Uploading")
    # excel_report("Alarm")
    # excel_report("Completed")

    # ws4 = wb.active
    # ws4.title = "Registration Report"
    # ws4['A46'].value = ""
    # ws4['A47'].value = "Ending 4"
    # ws4.append(['', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Remarks'])

    # excel_report("Due For Regs")
    # excel_report("Registered")
    # excel_report("unRegistered")
    # excel_report("Uploading")
    # excel_report("Alarm")
    # excel_report("Completed")

    # ws5 = wb.active
    # ws5.title = "Registration Report"
    # ws5['A56'].value = ""
    # ws5['A57'].value = "Ending 5"
    # ws5.append(['', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Remarks'])

    # excel_report("Due For Regs")
    # excel_report("Registered")
    # excel_report("unRegistered")
    # excel_report("Uploading")
    # excel_report("Alarm")
    # excel_report("Completed")

    # ws6 = wb.active
    # ws6.title = "Registration Report"
    # ws6['A66'].value = ""
    # ws6['A67'].value = "Ending 6"
    # ws6.append(['', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Remarks'])

    # excel_report("Due For Regs")
    # excel_report("Registered")
    # excel_report("unRegistered")
    # excel_report("Uploading")
    # excel_report("Alarm")
    # excel_report("Completed")

    # ws7 = wb.active
    # ws7.title = "Registration Report"
    # ws7['A76'].value = ""
    # ws7['A77'].value = "Ending 7"
    # ws7.append(['', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Remarks'])

    # excel_report("Due For Regs")
    # excel_report("Registered")
    # excel_report("unRegistered")
    # excel_report("Uploading")
    # excel_report("Alarm")
    # excel_report("Completed")

    # ws8 = wb.active
    # ws8.title = "Registration Report"
    # ws8['A86'].value = ""
    # ws8['A87'].value = "Ending 8"
    # ws8.append(['', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Remarks'])

    # excel_report("Due For Regs")
    # excel_report("Registered")
    # excel_report("unRegistered")
    # excel_report("Uploading")
    # excel_report("Alarm")
    # excel_report("Completed")

    # ws9 = wb.active
    # ws9.title = "Registration Report"
    # ws9['A96'].value = ""
    # ws9['A97'].value = "Ending 9"
    # ws9.append(['', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Remarks'])

    # excel_report("Due For Regs")
    # excel_report("Registered")
    # excel_report("unRegistered")
    # excel_report("Uploading")
    # excel_report("Alarm")
    # excel_report("Completed")


    wb.save(f"/Users/{username}/Desktop/Registration_Report.xlsx")
    return redirect('/Registration/January')
