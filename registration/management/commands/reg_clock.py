
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
from django.template import Context
from django.db.models import Q
from vehicle_masterlist.models import VehicleMasterList


django.setup()
sched = BlockingScheduler()
# @sched.scheduled_job('cron', day_of_week='mon-sun', hour=23)
        ################################
###.......1st Email, 1st day of Month before Due.....#####
        ################################
@sched.scheduled_job('interval', minutes=1)
def send_registration_email():
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    year1 = datetime.datetime.now().year - 1
    year2 = datetime.datetime.now().year - 2
    date_now = datetime.datetime.now().date()
    sent_status = VehicleMasterList.objects.all()
    if month == 12:
        print("1st Email Registration Month 1")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="1", Status="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.plate_no)
                plate = carreg.PLATE_NO
                print(plate)
        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                    'model':item.MODEL,
                    'make':item.VEHICLE_MAKE,
                    'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsjxmtsi@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status="Yes")
                car_status.update(Date_email_log= date_now)
                print("1st Email Registration Month 1 Send")

    elif month == 1:
        print("1st Email Registration Month 2")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="2", Status="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                    'model':item.MODEL,
                    'make':item.VEHICLE_MAKE,
                    'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status="Yes")
                car_status.update(Date_email_log= date_now)
                print("1st Email Registration Month 2 Send")

    elif month == 2:
        print("1st Email Registration Month 3")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="3", Status="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                    'model':item.MODEL,
                    'make':item.VEHICLE_MAKE,
                    'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status="Yes")
                car_status.update(Date_email_log= date_now)
                print("1st Email Registration Month 3 Send")

    elif month == 3:
        print("1st Email Registration Month 4")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="4", Status="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                    'model':item.MODEL,
                    'make':item.VEHICLE_MAKE,
                    'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status="Yes")
                car_status.update(Date_email_log= date_now)
                print("1st Email Registration Month 4 Send")

    elif month == 4:
        print("1st Email Registration Month 5")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="5", Status="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                    'model':item.MODEL,
                    'make':item.VEHICLE_MAKE,
                    'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status="Yes")
                car_status.update(Date_email_log= date_now)
                print("1st Email Registration Month 5 Send")

    elif month == 5:
        print("1st Email Registration Month 6")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="6", Status="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                    'model':item.MODEL,
                    'make':item.VEHICLE_MAKE,
                    'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status="Yes")
                car_status.update(Date_email_log= date_now)
                print("1st Email Registration Month 6 Send")

    elif month == 6:
        print("1st Email Registration Month 7")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="7", Status="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                    'model':item.MODEL,
                    'make':item.VEHICLE_MAKE,
                    'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status="Yes")
                car_status.update(Date_email_log= date_now)
                print("1st Email Registration Month 7 Send")

    elif month == 7:
        print("1st Email Registration Month 8")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="8", Status="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                    'model':item.MODEL,
                    'make':item.VEHICLE_MAKE,
                    'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status="Yes")
                car_status.update(Date_email_log= date_now)
                print("1st Email Registration Month 8 Send")

    elif month == 8:
        print("1st Email Registration Month 9")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="9", Status="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                    'model':item.MODEL,
                    'make':item.VEHICLE_MAKE,
                    'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status="Yes")
                car_status.update(Date_email_log= date_now)
                print("1st Email Registration Month 9 Send")

    elif month == 9:
        print("1st Email Registration Month 0")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="0", Status="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                    'model':item.MODEL,
                    'make':item.VEHICLE_MAKE,
                    'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email - ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status="Yes")
                car_status.update(Date_email_log= date_now)
                print("1st Email Registration Month 0 Send")

            #################################
            #####.......2nd email......######
            #################################
@sched.scheduled_job('interval', minutes=5)
def second_send_registration_email():
    ###---Get 14 days of the month---###
    given_date = datetime.datetime.now().date()
    sec_week_of_month = given_date.replace(day=14)
    ##---------------------------------------##
    ##---Get Current Month and Year -3-----###
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    year1 = datetime.datetime.now().year - 1
    year2 = datetime.datetime.now().year - 2
    ###------------------------------------##
    date_now = datetime.datetime.now().date()
    # print(year, year1, year2)
    sent_status = VehicleMasterList.objects.all()
    if month == 12:
        if given_date == sec_week_of_month:
            print("2nd Email Registration Month 1")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
                PLATE_ENDING="1", Status_2="No").exclude(exc)
            plate = ""
            for carreg in car_status:
                    # print(carreg.plate_no)
                    plate = carreg.PLATE_NO
                    print(plate)
            if plate != "":
                for item in car_status:
                    data ={
                        'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                    }
                    subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                    html_message = render_to_string('email.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsjxmtsi@gmail.com>'
                    cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    car_status.update(Status_2="Yes")
                    car_status.update(Date_email_log= date_now)
                    print("2nd Email Registration Month 1 Send")

    elif month == 1:
        if given_date == sec_week_of_month:
            print("2nd Email Registration Month 2")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
                PLATE_ENDING="2", Status_2="No").exclude(exc)
            plate = ""
            for carreg in car_status:
                    # print(carreg.PLATE_NO)
                    plate = carreg.PLATE_NO
                    print(plate)

            if plate != "":
                for item in car_status:
                    data ={
                        'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                    }
                    subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                    html_message = render_to_string('email.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                    cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    car_status.update(Status_2="Yes")
                    car_status.update(Date_email_log= date_now)
                    print("2nd Email Registration Month 2 Send")

    elif month == 2:
        if given_date == sec_week_of_month:
            print("2nd Email Registration Month 3")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
                PLATE_ENDING="3", Status_2="No").exclude(exc)
            plate = ""
            for carreg in car_status:
                    # print(carreg.PLATE_NO)
                    plate = carreg.PLATE_NO
                    print(plate)

            if plate != "":
                for item in car_status:
                    data ={
                        'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                    }
                    subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                    html_message = render_to_string('email.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                    cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    car_status.update(Status_2="Yes")
                    car_status.update(Date_email_log= date_now)
                    print("2nd Email Registration Month 3 Send")

    elif month == 3:
        if given_date == sec_week_of_month:
            print("2nd Email Registration Month 4")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
                PLATE_ENDING="4", Status_2="No").exclude(exc)
            plate = ""
            for carreg in car_status:
                    # print(carreg.PLATE_NO)
                    plate = carreg.PLATE_NO
                    print(plate)

            if plate != "":
                for item in car_status:
                    data ={
                        'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                    }
                    subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                    html_message = render_to_string('email.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                    cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    car_status.update(Status_2="Yes")
                    car_status.update(Date_email_log= date_now)
                    print("2nd Email Registration Month 4 Send")

    elif month == 4:
        if given_date == sec_week_of_month:
            print("2nd Email Registration Month 5")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
                PLATE_ENDING="5", Status_2="No").exclude(exc)
            plate = ""
            for carreg in car_status:
                    # print(carreg.PLATE_NO)
                    plate = carreg.PLATE_NO
                    print(plate)

            if plate != "":
                for item in car_status:
                    data ={
                        'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                    }
                    subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                    html_message = render_to_string('email.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                    cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    car_status.update(Status_2="Yes")
                    car_status.update(Date_email_log= date_now)
                    print("2nd Email Registration Month 5 Send")

    elif month == 5:
        if given_date == sec_week_of_month:
            print("2nd Email Registration Month 6")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
                PLATE_ENDING="6", Status_2="No").exclude(exc)
            plate = ""
            for carreg in car_status:
                    # print(carreg.PLATE_NO)
                    plate = carreg.PLATE_NO
                    print(plate)

            if plate != "":
                for item in car_status:
                    data ={
                        'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                    }
                    subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                    html_message = render_to_string('email.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                    cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    car_status.update(Status_2="Yes")
                    car_status.update(Date_email_log= date_now)
                    print("2nd Email Registration Month 6 Send")

    elif month == 6:
        if given_date == sec_week_of_month:
            print("2nd Email Registration Month 7")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
                PLATE_ENDING="7", Status_2="No").exclude(exc)
            plate = ""
            for carreg in car_status:
                    # print(carreg.PLATE_NO)
                    plate = carreg.PLATE_NO
                    print(plate)

            if plate != "":
                for item in car_status:
                    data ={
                        'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                    }
                    subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                    html_message = render_to_string('email.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                    cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    car_status.update(Status_2="Yes")
                    car_status.update(Date_email_log= date_now)
                    print("2nd Email Registration Month 7 Send")

    elif month == 7:
        if given_date == sec_week_of_month:
            print("2nd Email Registration Month 8")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
                PLATE_ENDING="8", Status_2="No").exclude(exc)
            plate = ""
            for carreg in car_status:
                    # print(carreg.PLATE_NO)
                    plate = carreg.PLATE_NO
                    print(plate)

            if plate != "":
                for item in car_status:
                    data ={
                        'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                    }
                    subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                    html_message = render_to_string('email.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                    cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    car_status.update(Status_2="Yes")
                    car_status.update(Date_email_log= date_now)
                    print("2nd Email Registration Month 8 Send")

    elif month == 8:
        if given_date == sec_week_of_month:
            print("2nd Email Registration Month 9")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
                PLATE_ENDING="9", Status_2="No").exclude(exc)
            plate = ""
            for carreg in car_status:
                    # print(carreg.PLATE_NO)
                    plate = carreg.PLATE_NO
                    print(plate)

            if plate != "":
                for item in car_status:
                    data ={
                        'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                    }
                    subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                    html_message = render_to_string('email.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                    cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    car_status.update(Status_2="Yes")
                    car_status.update(Date_email_log= date_now)
                    print("2nd Email Registration Month 9 Send")

    elif month == 9:
        print("2nd Email Registration Month 0 Test date")
        if given_date == sec_week_of_month:
            print("2nd Email Registration Month 0")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
                PLATE_ENDING="0", Status_2="No").exclude(exc)
            plate = ""
            for carreg in car_status:
                    # print(carreg.PLATE_NO)
                    plate = carreg.PLATE_NO
                    print(plate)

            if plate != "":
                for item in car_status:
                    data ={
                        'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                    }
                    subject = 'Fleet Management System Automated Email - ' + (item.PLATE_NO)
                    html_message = render_to_string('email.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                    cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    car_status.update(Status_2="Yes")
                    car_status.update(Date_email_log= date_now)
                    print("2nd Email Registration Month 0 Send")

        #################################
####.......3rd Email, 1st day of Month Due.....#####
        #################################
@sched.scheduled_job('interval', minutes=10)
def third_send_registration_email():
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    year1 = datetime.datetime.now().year - 1
    year2 = datetime.datetime.now().year - 2
    date_now = datetime.datetime.now().date()
    # print(year, year1, year2)
    sent_status = VehicleMasterList.objects.all()
    if month == 1:
        print("3rd Email Registration Month 1")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2) | Q(BAND_LEVEL="Band D") | Q(BAND_LEVEL="Band E") | Q(BAND_LEVEL="Band F")
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="1", Status_3="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.plate_no)
                plate = carreg.PLATE_NO
                print(plate)
        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsjxmtsi@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status_3="Yes")
                car_status.update(Date_email_log= date_now)
                print("3rd Email Registration Month 1 Send")

    elif month == 2:
        print("3rd Email Registration Month 2")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2) | Q(BAND_LEVEL="Band D") | Q(BAND_LEVEL="Band E") | Q(BAND_LEVEL="Band F")
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="2", Status_3="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status_3="Yes")
                car_status.update(Date_email_log= date_now)
                print("3rd Email Registration Month 2 Send")

    elif month == 3:
        print("3rd Email Registration Month 3")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2) | Q(BAND_LEVEL="Band D") | Q(BAND_LEVEL="Band E") | Q(BAND_LEVEL="Band F")
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="3", Status_3="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status_3="Yes")
                car_status.update(Date_email_log= date_now)
                print("3rd Email Registration Month 3 Send")

    elif month == 4:
        print("3rd Email Registration Month 4")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2) | Q(BAND_LEVEL="Band D") | Q(BAND_LEVEL="Band E") | Q(BAND_LEVEL="Band F")
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="4", Status_3="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status_3="Yes")
                car_status.update(Date_email_log= date_now)
                print("3rd Email Registration Month 4 Send")

    elif month == 5:
        print("3rd Email Registration Month 5")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2) | Q(BAND_LEVEL="Band D") | Q(BAND_LEVEL="Band E") | Q(BAND_LEVEL="Band F")
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="5", Status_3="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status_3="Yes")
                car_status.update(Date_email_log= date_now)
                print("3rd Email Registration Month 5 Send")

    elif month == 6:
        print("3rd Email Registration Month 6")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2) | Q(BAND_LEVEL="Band D") | Q(BAND_LEVEL="Band E") | Q(BAND_LEVEL="Band F")
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="6", Status_3="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status_3="Yes")
                car_status.update(Date_email_log= date_now)
                print("3rd Email Registration Month 6 Send")

    elif month == 7:
        print("3rd Email Registration Month 7")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2) | Q(BAND_LEVEL="Band D") | Q(BAND_LEVEL="Band E") | Q(BAND_LEVEL="Band F")
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="7", Status_3="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status_3="Yes")
                car_status.update(Date_email_log= date_now)
                print("3rd Email Registration Month 7 Send")

    elif month == 8:
        print("3rd Email Registration Month 8")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2) | Q(BAND_LEVEL="Band D") | Q(BAND_LEVEL="Band E") | Q(BAND_LEVEL="Band F")
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="8", Status_3="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email - ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status_3="Yes")
                car_status.update(Date_email_log= date_now)
                print("3rd Email Registration Month 8 Send")

    elif month == 9:
        print("3rd Email Registration Month 9")
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="9", Status_3="No")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2) | Q(BAND_LEVEL="Band D") | Q(BAND_LEVEL="Band E") | Q(BAND_LEVEL="Band F")
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="9", Status_3="No").exclude(exc)
        print(car_status)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email- ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status_3="Yes")
                car_status.update(Date_email_log= date_now)
                print("3rd Email Registration Month 9 Send")

    elif month == 10:
        print("3rd Email Registration Month 0")
        exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2) | Q(BAND_LEVEL="Band D") | Q(BAND_LEVEL="Band E") | Q(BAND_LEVEL="Band F")
        car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
            PLATE_ENDING="0", Status_3="No").exclude(exc)
        plate = ""
        for carreg in car_status:
                # print(carreg.PLATE_NO)
                plate = carreg.PLATE_NO
                print(plate)

        if plate != "":
            for item in car_status:
                data ={
                    'plate':item.PLATE_NO,
                        'model':item.MODEL,
                        'make':item.VEHICLE_MAKE,
                        'brand':item.BRAND
                }
                subject = 'Fleet Management System Automated Email - ' + (item.PLATE_NO)
                html_message = render_to_string('email.html',data)
                plain_message = item.PLATE_NO
                recipient_list = [item.EMAIL]
                from_email = 'Fleet Management System <fmsconnected@gmail.com>'
                cc_email= ['zscsantos@globe.com.ph','zfvdelacruz@globe.com.ph']
                toaddrs = recipient_list + cc_email
                mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                car_status.update(Status_3="Yes")
                car_status.update(Date_email_log= date_now)
                print("3rd Registration Month 0 Send")

sched.start()