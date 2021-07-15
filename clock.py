
from django.core.mail import get_connection,send_mail
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
from models import (
        Vehicle_Repair
)


sched = BlockingScheduler()
# def request_cron_email():
# class Command(BaseCommand):
sched = Scheduler()
@sched.cron_schedule(day_of_week='mon-sun', hour=24)
def email_job():
    car_status = Vehicle_Repair.objects.filter(Deadline__date = datetime.datetime.today(), sent_email="No")
    plate = ""
    for carreg in car_status:
            # print(carreg.plate_no)
            plate = carreg.plate_no
            print(plate)

    if plate != "":
        for item in car_status:
            subject = 'Fleet Management System Automated Email'
            html_message = render_to_string('request/vehicle_repair/pms_email.html',{'content':item.plate_no})
            plain_message = item.plate_no
            recipient_list = [item.email]
            from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
            mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
            car_status.update(sent_email="Yes")
            car_status.update(Date_email_log= datetime.datetime.today())

    print('This job working')

sched.start()
# while __name__ == '__main__':
#     pass