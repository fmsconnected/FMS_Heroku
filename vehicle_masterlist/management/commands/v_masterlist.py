
from django.core.mail import get_connection,send_mail
from django.core.management.base import BaseCommand
from apscheduler.schedulers.blocking import BlockingScheduler
from django.core import mail
import datetime
from datetime import date, timedelta
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import django
import sched
from django.template import Context
from django.db.models import Q
from vehicle_masterlist.models import VehicleMasterList


django.setup()
sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=15)
def send_masterlist_email():
    given_date = datetime.datetime.now().date()
    sec_week_of_month = given_date.replace(day=1)
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    year1 = datetime.datetime.now().year - 1
    year2 = datetime.datetime.now().year - 2
    date_now = datetime.datetime.now().date()
    sent_status = VehicleMasterList.objects.all()
    print("year",year)
    print("year1",year1)
    print("year2",year2)
    if month == 1:
        # if given_date == sec_week_of_month:
        print("1st Email VehicleMasterList")
        # car_status = VehicleMasterList.objects.filter(vehicle_status="Active", Status_4="No")[:80]
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="2", Status="No").exclude(exc)[:80]
        print(car_status)
        plate = ""
        for carreg in car_status:
                # print(carreg.plate_no)
                plate = carreg.PLATE_NO
                print(plate)
        if car_status != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                    'cs':item.CS_NO,
                    'cr_name':item.CR_NAME,
                    'model':item.MODEL,
                    'brand':item.BRAND,
                    'make':item.VEHICLE_MAKE,
                    'type':item.VEHICLE_TYPE,
                    'lname':item.ASSIGNEE_LAST_NAME,
                    'fname':item.ASSIGNEE_FIRST_NAME,
                    'emp_id':item.Employee,
                    'band':item.BAND_LEVEL,
                    'cost':item.COST_CENTER,
                    'group':item.GROUP,
                    'acq_date':item.ACQ_DATE,
                    'acq_cost':item.ACQ_COST,
                }
                subject = 'Reminder for Annual Vehicle Registration and Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
                html_message = render_to_string('email_template.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsjxmtsi@gmail.com>'
                cc_email= ['sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph','zscsantos@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                VehicleMasterList.objects.filter(PLATE_NO__in=list(car_status)).update(Status="Yes")
                print("1st Email VehicleMasterList Send")

sched.start()