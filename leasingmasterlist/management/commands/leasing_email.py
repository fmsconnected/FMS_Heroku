
from django.core.mail import get_connection,send_mail,EmailMessage,EmailMultiAlternatives
from django.core.management.base import BaseCommand
from apscheduler.schedulers.blocking import BlockingScheduler
from django.core import mail
import datetime
import os
from datetime import date, timedelta
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import django
import sched
from django.template import Context
from django.db.models import Q
from leasingmasterlist.models import Leasing

django.setup()
sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=1)
def send_leasing_email():
    date = datetime.datetime.today()
    month = datetime.datetime.now().month
    months = ['zero','January','February','March','April','May','June','July','August','September','October','November','December']
    month_name = months[date.month]
    year = datetime.datetime.now().year
    year4 = datetime.datetime.now().year - 5
    date_now = datetime.datetime.now().date()
    sent_status = Leasing.objects.all()
    print("1st Email Leasing")
    file_path = os.path.abspath('leasingmasterlist/management/files/Service_Vehicle_Request_Form_2021.xls')
    car_status = Leasing.objects.filter(ACQUISITION_DATE__year=year4)
    plate = ""
    for carreg in car_status:
            # print(carreg.plate_no)
            plate = carreg.PLATE_NUMBER
            print(plate)
    if plate != "":
        for item in car_status:
            data ={
                'month':month_name,
                'year':year4,
                'plate':item.PLATE_NUMBER,
                'cs':item.CS_NO,
                'model':item.MODEL,
                'brand':item.BRAND,
                'make':item.VEHICLE_MAKE,
                'type':item.VEHICLE_TYPE,
                'lname':item.LAST_NAME_ASSIGNEE,
                'fname':item.FIRST_NAME_ASSIGNEE,
                'acq_date':item.ACQUISITION_DATE,
            }
            subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NUMBER)
            html_message = render_to_string('email.html',data)
            plain_message = item.PLATE_NUMBER
            to_email = [item.email]
            from_email = 'Fleet Management System <fmsjxmtsi@gmail.com>'
            cc_email= ['zpaconcepcion@globe.com.ph ']
            toaddrs = to_email + cc_email
            mail = EmailMultiAlternatives(subject,html_message, from_email, toaddrs)
            # mail.attach_alternative('p.pdf')
            mail.content_subtype='html'
            mail.attach_file(file_path)
            email_res = mail.send()
            print("1st Email Leasing Send")

sched.start()