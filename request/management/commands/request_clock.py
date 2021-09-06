
from django.core.mail import get_connection,send_mail,EmailMessage,EmailMultiAlternatives
from django.core.management.base import BaseCommand
# from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from django.core import mail
import datetime
from datetime import date, timedelta
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from request.models import Vehicle_Repair
import django
import sched

django.setup()
sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=10)
# @sched.scheduled_job('cron', day_of_week='mon-sun', hour=23)

def email_job():
    print("Test Request Email Starting.....")
    current_date = datetime.datetime.today()
    date_now = datetime.datetime.now().date()
    # print(date_now)

    car_status = Vehicle_Repair.objects.filter(Deadline__year=current_date.year,Deadline__month=current_date.month, sent_email="No")
    plate = ""
    for carreg in car_status:
            # print(carreg.plate_no)
            plate = carreg.plate_no
            print(plate)

    if plate != "":
        for item in car_status:
            subject = 'Fleet Management System Automated Email'
            html_message = render_to_string('vehicle_repair/pms_email.html',{'content':item.plate_no})
            plain_message = item.plate_no
            recipient_list = [item.email]
            cc_email= ['zscsantos@globe.com.ph']
            from_email = 'Fleet Management System <fmsconnected@gmail.com>'
            toaddrs = recipient_list + cc_email
            mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message)
            car_status.update(sent_email="Yes") 
            car_status.update(Date_email_log=datetime.datetime.now().date())
            print("Test Request Email Send!")

sched.start()