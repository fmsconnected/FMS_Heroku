
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
from registration.models import Registration
import django
import sched
from vehicle_masterlist.models import VehicleMasterList

django.setup()
sched = BlockingScheduler()
# @sched.scheduled_job('cron', day_of_week='mon-sun', hour=23)
@sched.scheduled_job('interval', minutes=15)
def send_registration_email():
    month = datetime.datetime.now().month
    date_now = datetime.datetime.now().date()
    # print(date_now)
    sent_status = VehicleMasterList.objects.all()
    if month == 12:
        print("test Registration Month 1")
        car_status = VehicleMasterList.objects.filter(
            PLATE_ENDING="1", sent_email="No")
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
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsjxmtsi@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 1:
        print("test Registration Month 2")
        car_status = VehicleMasterList.objects.filter(
            PLATE_ENDING="2", sent_email="No")
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
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 2:
        print("test Registration Month 3")
        car_status = VehicleMasterList.objects.filter(
            PLATE_ENDING="3", sent_email="No")
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
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 3:
        print("test Registration Month 4")
        car_status = VehicleMasterList.objects.filter(
            PLATE_ENDING="4", sent_email="No")
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
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 4:
        print("test Registration Month 5")
        car_status = VehicleMasterList.objects.filter(
            PLATE_ENDING="5", sent_email="No")
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
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 5:
        print("test Registration Month 6")
        car_status = VehicleMasterList.objects.filter(
            PLATE_ENDING="6", sent_email="No")
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
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 6:
        print("test Registration Month 7")
        car_status = VehicleMasterList.objects.filter(
            PLATE_ENDING="7", sent_email="No")
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
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 7:
        print("test Registration Month 8")
        car_status = VehicleMasterList.objects.filter(
            PLATE_ENDING="8", sent_email="No")
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
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 8:
        print("test Registration Month 9")
        car_status = VehicleMasterList.objects.filter(
            PLATE_ENDING="9", sent_email="No")
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
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

    elif month == 9:
        print("test Registration Month 0")
        car_status = VehicleMasterList.objects.filter(
            PLATE_ENDING="0", sent_email="No")
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
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(sent_email="Yes")
                car_status.update(Date_email_log= date_now)

sched.start()