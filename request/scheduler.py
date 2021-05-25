import schedule
import time
from django.core.mail import get_connection,send_mail
from django.core import mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.core import mail
import datetime
from datetime import date, timedelta

from request import models

class request_cron_email():
    print("mart test")
    date_now = datetime.datetime.now().date()
    sent_status = models.Vehicle_Repair.objects.all(),
    car_status = models.Vehicle_Repair.objects.filter(Deadline__date = datetime.datetime.today(), sent_email="No")

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
            from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
            mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
            # car_status.update(sent_email="Yes")
            car_status.update(Date_email_log= date_now)

schedule.every(10).seconds.do(request_cron_email)

while 1:
	schedule.run_pending()
	time.sleep(1)