
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
# @sched.scheduled_job('interval', minutes=5)
# def send_masterlist_email():
#     given_date = datetime.datetime.now().date()
#     sec_week_of_month = given_date.replace(day=15)
#     month = datetime.datetime.now().month
#     year = datetime.datetime.now().year
#     year1 = datetime.datetime.now().year - 1
#     year2 = datetime.datetime.now().year - 2
#     date_now = datetime.datetime.now().date()
#     sent_status = VehicleMasterList.objects.all()
#     print("given_date",given_date)
#     print("sec_week_of_month",sec_week_of_month)
#                     ###########################
#                     ######## 1st Email ########
#                     ###########################
#     if month == 12:
#         print("1st Email VehicleMasterList")
#         exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#         car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
#             PLATE_ENDING="1", Status="No").exclude(exc)[:80]
#         print(car_status)
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.plate_no)
#                 plate = carreg.PLATE_NO
#                 print(plate)
#         if car_status != "":
#             for item in car_status:
#                 data ={
#                     'plate':item.PLATE_NO,
#                     'cs':item.CS_NO,
#                     'cr_name':item.CR_NAME,
#                     'model':item.MODEL,
#                     'brand':item.BRAND,
#                     'make':item.VEHICLE_MAKE,
#                     'type':item.VEHICLE_TYPE,
#                     'lname':item.ASSIGNEE_LAST_NAME,
#                     'fname':item.ASSIGNEE_FIRST_NAME,
#                     'emp_id':item.Employee,
#                     'band':item.BAND_LEVEL,
#                     'cost':item.COST_CENTER,
#                     'group':item.GROUP,
#                     'acq_date':item.ACQ_DATE,
#                     'acq_cost':item.ACQ_COST,
#                 }
#                 subject = 'Reminder for Annual Vehicle Registration and Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
#                 html_message = render_to_string('email_template.html',data)
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.EMAIL]
#                 from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                 cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                 toaddrs = recipient_list + cc_email
#                 mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                 VehicleMasterList.objects.filter(PLATE_NO__in=list(car_status)).update(Status="Yes")
#                 print("1st Email VehicleMasterList Send")
#     if month == 1:
#         print("1st Email VehicleMasterList")
#         exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#         car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
#             PLATE_ENDING="2", Status="No").exclude(exc)[:80]
#         print(car_status)
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.plate_no)
#                 plate = carreg.PLATE_NO
#                 print(plate)
#         if car_status != "":
#             for item in car_status:
#                 data ={
#                     'plate':item.PLATE_NO,
#                     'cs':item.CS_NO,
#                     'cr_name':item.CR_NAME,
#                     'model':item.MODEL,
#                     'brand':item.BRAND,
#                     'make':item.VEHICLE_MAKE,
#                     'type':item.VEHICLE_TYPE,
#                     'lname':item.ASSIGNEE_LAST_NAME,
#                     'fname':item.ASSIGNEE_FIRST_NAME,
#                     'emp_id':item.Employee,
#                     'band':item.BAND_LEVEL,
#                     'cost':item.COST_CENTER,
#                     'group':item.GROUP,
#                     'acq_date':item.ACQ_DATE,
#                     'acq_cost':item.ACQ_COST,
#                 }
#                 subject = 'Reminder for Annual Vehicle Registration and Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
#                 html_message = render_to_string('email_template.html',data)
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.EMAIL]
#                 from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                 cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                 toaddrs = recipient_list + cc_email
#                 mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                 VehicleMasterList.objects.filter(PLATE_NO__in=list(car_status)).update(Status="Yes")
#                 print("1st Email VehicleMasterList Send")
#     if month == 2:
#         print("1st Email VehicleMasterList")
#         exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#         car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
#             PLATE_ENDING="3", Status="No").exclude(exc)[:80]
#         print(car_status)
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.plate_no)
#                 plate = carreg.PLATE_NO
#                 print(plate)
#         if car_status != "":
#             for item in car_status:
#                 data ={
#                     'plate':item.PLATE_NO,
#                     'cs':item.CS_NO,
#                     'cr_name':item.CR_NAME,
#                     'model':item.MODEL,
#                     'brand':item.BRAND,
#                     'make':item.VEHICLE_MAKE,
#                     'type':item.VEHICLE_TYPE,
#                     'lname':item.ASSIGNEE_LAST_NAME,
#                     'fname':item.ASSIGNEE_FIRST_NAME,
#                     'emp_id':item.Employee,
#                     'band':item.BAND_LEVEL,
#                     'cost':item.COST_CENTER,
#                     'group':item.GROUP,
#                     'acq_date':item.ACQ_DATE,
#                     'acq_cost':item.ACQ_COST,
#                 }
#                 subject = 'Reminder for Annual Vehicle Registration and Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
#                 html_message = render_to_string('email_template.html',data)
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.EMAIL]
#                 from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                 cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                 toaddrs = recipient_list + cc_email
#                 mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                 VehicleMasterList.objects.filter(PLATE_NO__in=list(car_status)).update(Status="Yes")
#                 print("1st Email VehicleMasterList Send")
#     if month == 3:
#         print("1st Email VehicleMasterList")
#         exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#         car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
#             PLATE_ENDING="4", Status="No").exclude(exc)[:80]
#         print(car_status)
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.plate_no)
#                 plate = carreg.PLATE_NO
#                 print(plate)
#         if car_status != "":
#             for item in car_status:
#                 data ={
#                     'plate':item.PLATE_NO,
#                     'cs':item.CS_NO,
#                     'cr_name':item.CR_NAME,
#                     'model':item.MODEL,
#                     'brand':item.BRAND,
#                     'make':item.VEHICLE_MAKE,
#                     'type':item.VEHICLE_TYPE,
#                     'lname':item.ASSIGNEE_LAST_NAME,
#                     'fname':item.ASSIGNEE_FIRST_NAME,
#                     'emp_id':item.Employee,
#                     'band':item.BAND_LEVEL,
#                     'cost':item.COST_CENTER,
#                     'group':item.GROUP,
#                     'acq_date':item.ACQ_DATE,
#                     'acq_cost':item.ACQ_COST,
#                 }
#                 subject = 'Reminder for Annual Vehicle Registration and Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
#                 html_message = render_to_string('email_template.html',data)
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.EMAIL]
#                 from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                 cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                 toaddrs = recipient_list + cc_email
#                 mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                 VehicleMasterList.objects.filter(PLATE_NO__in=list(car_status)).update(Status="Yes")
#                 print("1st Email VehicleMasterList Send")
#     if month == 4:
#         print("1st Email VehicleMasterList")
#         exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#         car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
#             PLATE_ENDING="5", Status="No").exclude(exc)[:80]
#         print(car_status)
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.plate_no)
#                 plate = carreg.PLATE_NO
#                 print(plate)
#         if car_status != "":
#             for item in car_status:
#                 data ={
#                     'plate':item.PLATE_NO,
#                     'cs':item.CS_NO,
#                     'cr_name':item.CR_NAME,
#                     'model':item.MODEL,
#                     'brand':item.BRAND,
#                     'make':item.VEHICLE_MAKE,
#                     'type':item.VEHICLE_TYPE,
#                     'lname':item.ASSIGNEE_LAST_NAME,
#                     'fname':item.ASSIGNEE_FIRST_NAME,
#                     'emp_id':item.Employee,
#                     'band':item.BAND_LEVEL,
#                     'cost':item.COST_CENTER,
#                     'group':item.GROUP,
#                     'acq_date':item.ACQ_DATE,
#                     'acq_cost':item.ACQ_COST,
#                 }
#                 subject = 'Reminder for Annual Vehicle Registration and Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
#                 html_message = render_to_string('email_template.html',data)
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.EMAIL]
#                 from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                 cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                 toaddrs = recipient_list + cc_email
#                 mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                 VehicleMasterList.objects.filter(PLATE_NO__in=list(car_status)).update(Status="Yes")
#                 print("1st Email VehicleMasterList Send")
#     if month == 5:
#         print("1st Email VehicleMasterList")
#         exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#         car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
#             PLATE_ENDING="6", Status="No").exclude(exc)[:80]
#         print(car_status)
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.plate_no)
#                 plate = carreg.PLATE_NO
#                 print(plate)
#         if car_status != "":
#             for item in car_status:
#                 data ={
#                     'plate':item.PLATE_NO,
#                     'cs':item.CS_NO,
#                     'cr_name':item.CR_NAME,
#                     'model':item.MODEL,
#                     'brand':item.BRAND,
#                     'make':item.VEHICLE_MAKE,
#                     'type':item.VEHICLE_TYPE,
#                     'lname':item.ASSIGNEE_LAST_NAME,
#                     'fname':item.ASSIGNEE_FIRST_NAME,
#                     'emp_id':item.Employee,
#                     'band':item.BAND_LEVEL,
#                     'cost':item.COST_CENTER,
#                     'group':item.GROUP,
#                     'acq_date':item.ACQ_DATE,
#                     'acq_cost':item.ACQ_COST,
#                 }
#                 subject = 'Reminder for Annual Vehicle Registration and Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
#                 html_message = render_to_string('email_template.html',data)
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.EMAIL]
#                 from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                 cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                 toaddrs = recipient_list + cc_email
#                 mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                 VehicleMasterList.objects.filter(PLATE_NO__in=list(car_status)).update(Status="Yes")
#                 print("1st Email VehicleMasterList Send")
#     if month == 6:
#         print("1st Email VehicleMasterList")
#         exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#         car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
#             PLATE_ENDING="7", Status="No").exclude(exc)[:80]
#         print(car_status)
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.plate_no)
#                 plate = carreg.PLATE_NO
#                 print(plate)
#         if car_status != "":
#             for item in car_status:
#                 data ={
#                     'plate':item.PLATE_NO,
#                     'cs':item.CS_NO,
#                     'cr_name':item.CR_NAME,
#                     'model':item.MODEL,
#                     'brand':item.BRAND,
#                     'make':item.VEHICLE_MAKE,
#                     'type':item.VEHICLE_TYPE,
#                     'lname':item.ASSIGNEE_LAST_NAME,
#                     'fname':item.ASSIGNEE_FIRST_NAME,
#                     'emp_id':item.Employee,
#                     'band':item.BAND_LEVEL,
#                     'cost':item.COST_CENTER,
#                     'group':item.GROUP,
#                     'acq_date':item.ACQ_DATE,
#                     'acq_cost':item.ACQ_COST,
#                 }
#                 subject = 'Reminder for Annual Vehicle Registration and Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
#                 html_message = render_to_string('email_template.html',data)
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.EMAIL]
#                 from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                 cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                 toaddrs = recipient_list + cc_email
#                 mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                 VehicleMasterList.objects.filter(PLATE_NO__in=list(car_status)).update(Status="Yes")
#                 print("1st Email VehicleMasterList Send")
#     if month == 7:
#         print("1st Email VehicleMasterList")
#         exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#         car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
#             PLATE_ENDING="8", Status="No").exclude(exc)[:80]
#         print(car_status)
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.plate_no)
#                 plate = carreg.PLATE_NO
#                 print(plate)
#         if car_status != "":
#             for item in car_status:
#                 data ={
#                     'plate':item.PLATE_NO,
#                     'cs':item.CS_NO,
#                     'cr_name':item.CR_NAME,
#                     'model':item.MODEL,
#                     'brand':item.BRAND,
#                     'make':item.VEHICLE_MAKE,
#                     'type':item.VEHICLE_TYPE,
#                     'lname':item.ASSIGNEE_LAST_NAME,
#                     'fname':item.ASSIGNEE_FIRST_NAME,
#                     'emp_id':item.Employee,
#                     'band':item.BAND_LEVEL,
#                     'cost':item.COST_CENTER,
#                     'group':item.GROUP,
#                     'acq_date':item.ACQ_DATE,
#                     'acq_cost':item.ACQ_COST,
#                 }
#                 subject = 'Reminder for Annual Vehicle Registration and Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
#                 html_message = render_to_string('email_template.html',data)
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.EMAIL]
#                 from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                 cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                 toaddrs = recipient_list + cc_email
#                 mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                 VehicleMasterList.objects.filter(PLATE_NO__in=list(car_status)).update(Status="Yes")
#                 print("1st Email VehicleMasterList Send")
#     if month == 8:
#         print("1st Email VehicleMasterList")
#         exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#         car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
#             PLATE_ENDING="9", Status="No").exclude(exc)[:80]
#         print(car_status)
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.plate_no)
#                 plate = carreg.PLATE_NO
#                 print(plate)
#         if car_status != "":
#             for item in car_status:
#                 data ={
#                     'plate':item.PLATE_NO,
#                     'cs':item.CS_NO,
#                     'cr_name':item.CR_NAME,
#                     'model':item.MODEL,
#                     'brand':item.BRAND,
#                     'make':item.VEHICLE_MAKE,
#                     'type':item.VEHICLE_TYPE,
#                     'lname':item.ASSIGNEE_LAST_NAME,
#                     'fname':item.ASSIGNEE_FIRST_NAME,
#                     'emp_id':item.Employee,
#                     'band':item.BAND_LEVEL,
#                     'cost':item.COST_CENTER,
#                     'group':item.GROUP,
#                     'acq_date':item.ACQ_DATE,
#                     'acq_cost':item.ACQ_COST,
#                 }
#                 subject = 'Reminder for Annual Vehicle Registration and Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
#                 html_message = render_to_string('email_template.html',data)
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.EMAIL]
#                 from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                 cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                 toaddrs = recipient_list + cc_email
#                 mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                 VehicleMasterList.objects.filter(PLATE_NO__in=list(car_status)).update(Status="Yes")
#                 print("1st Email VehicleMasterList Send")
#     if month == 9:
#         print("1st Email VehicleMasterList")
#         exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#         car_status = VehicleMasterList.objects.filter(vehicle_status="Active",
#             PLATE_ENDING="0", Status="No").exclude(exc)[:80]
#         print(car_status)
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.plate_no)
#                 plate = carreg.PLATE_NO
#                 print(plate)
#         if car_status != "":
#             for item in car_status:
#                 data ={
#                     'plate':item.PLATE_NO,
#                     'cs':item.CS_NO,
#                     'cr_name':item.CR_NAME,
#                     'model':item.MODEL,
#                     'brand':item.BRAND,
#                     'make':item.VEHICLE_MAKE,
#                     'type':item.VEHICLE_TYPE,
#                     'lname':item.ASSIGNEE_LAST_NAME,
#                     'fname':item.ASSIGNEE_FIRST_NAME,
#                     'emp_id':item.Employee,
#                     'band':item.BAND_LEVEL,
#                     'cost':item.COST_CENTER,
#                     'group':item.GROUP,
#                     'acq_date':item.ACQ_DATE,
#                     'acq_cost':item.ACQ_COST,
#                 }
#                 subject = 'Reminder for Annual Vehicle Registration and Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
#                 html_message = render_to_string('email_template.html',data)
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.EMAIL]
#                 from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                 cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                 toaddrs = recipient_list + cc_email
#                 mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                 VehicleMasterList.objects.filter(PLATE_NO__in=list(car_status)).update(Status="Yes")
#                 print("1st Email VehicleMasterList Send")

###########################
######## 2nd Email ########
### Status Confirmation ###
###########################
@sched.scheduled_job('interval', minutes=5)
def account_email():
    given_date = datetime.datetime.now().date()
    sec_week_of_month = given_date.replace(day=15)
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    year1 = datetime.datetime.now().year - 1
    year2 = datetime.datetime.now().year - 2
    date_now = datetime.datetime.now().date()
    sent_status = VehicleMasterList.objects.all()
    if month == 12:
        if sec_week_of_month == given_date:
            print("2nd Email Account Confirmation")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2) 
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",confirmation="No",smoke="Yes",
                PLATE_ENDING="1", Status="Yes").exclude(exc)[:80]
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
                    subject = 'Reminder for Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
                    html_message = render_to_string('account_template.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
                    cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    print("2nd Email Account Confirmation Send")  
    if month == 1:
        if sec_week_of_month == given_date:
            print("2nd Email Account Confirmation")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",confirmation="No",smoke="Yes",
                PLATE_ENDING="2").exclude(exc)[:80]
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
                    subject = 'Reminder for Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
                    html_message = render_to_string('account_template.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
                    cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    print("2nd Email Account Confirmation Send")
    if month == 2:
        if sec_week_of_month == given_date:
            print("2nd Email Account Confirmation")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",confirmation="No",smoke="Yes",
                PLATE_ENDING="3", Status="Yes").exclude(exc)[:80]
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
                    subject = 'Reminder for Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
                    html_message = render_to_string('account_template.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
                    cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    print("2nd Email Account Confirmation Send")

    if month == 3:
        if sec_week_of_month == given_date:
            print("2nd Email Account Confirmation")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",confirmation="No",smoke="Yes",
                PLATE_ENDING="4", Status="Yes").exclude(exc)[:80]
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
                    subject = 'Reminder for Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
                    html_message = render_to_string('account_template.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
                    cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    print("2nd Email Account Confirmation Send")
    if month == 4:
        if sec_week_of_month == given_date:
            print("2nd Email Account Confirmation")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",confirmation="No",smoke="Yes",
                PLATE_ENDING="5", Status="Yes").exclude(exc)[:80]
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
                    subject = 'Reminder for Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
                    html_message = render_to_string('account_template.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
                    cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    print("2nd Email Account Confirmation Send")
    if month == 5:
        if sec_week_of_month == given_date:
            print("2nd Email Account Confirmation")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",confirmation="No",smoke="Yes",
                PLATE_ENDING="6", Status="Yes").exclude(exc)[:80]
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
                    subject = 'Reminder for Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
                    html_message = render_to_string('account_template.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
                    cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    print("2nd Email Account Confirmation Send")
    if month == 6:
        if sec_week_of_month == given_date:
            print("2nd Email Account Confirmation")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",confirmation="No",smoke="Yes",
                PLATE_ENDING="7", Status="Yes").exclude(exc)[:80]
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
                    subject = 'Reminder for Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
                    html_message = render_to_string('account_template.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
                    cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    print("2nd Email Account Confirmation Send")
    if month == 7:
        if sec_week_of_month == given_date:
            print("2nd Email Account Confirmation")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",confirmation="No",smoke="Yes",
                PLATE_ENDING="8", Status="Yes").exclude(exc)[:80]
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
                    subject = 'Reminder for Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
                    html_message = render_to_string('account_template.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
                    cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    print("2nd Email Account Confirmation Send")
    if month == 8:
        if sec_week_of_month == given_date:
            print("2nd Email Account Confirmation")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",confirmation="No",smoke="Yes",
                PLATE_ENDING="9", Status="Yes").exclude(exc)[:80]
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
                    subject = 'Reminder for Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
                    html_message = render_to_string('account_template.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
                    cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    print("2nd Email Account Confirmation Send")
    if month == 9:
        if sec_week_of_month == given_date:
            print("2nd Email Account Confirmation")
            exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
            car_status = VehicleMasterList.objects.filter(vehicle_status="Active",confirmation="No",smoke="Yes",
                PLATE_ENDING="0", Status="Yes").exclude(exc)[:80]
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
                    subject = 'Reminder for Vehicle Confirmation - ' + "(" +(item.PLATE_NO) + ")"
                    html_message = render_to_string('account_template.html',data)
                    plain_message = item.PLATE_NO
                    recipient_list = [item.EMAIL]
                    from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
                    cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
                    toaddrs = recipient_list + cc_email
                    mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
                    print("2nd Email Account Confirmation Send")

###########################
######## 2nd Email ########
### Registration Confirmation ####
###########################
# @sched.scheduled_job('interval', minutes=5)
# def reg_email():
#     given_date = datetime.datetime.now().date()
#     sec_week_of_month = given_date.replace(day=15)
#     month = datetime.datetime.now().month
#     year = datetime.datetime.now().year
#     year1 = datetime.datetime.now().year - 1
#     year2 = datetime.datetime.now().year - 2
#     date_now = datetime.datetime.now().date()
#     sent_status = VehicleMasterList.objects.all()
#     if month == 12:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="Yes",
#                 PLATE_ENDING="1", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('registration_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration Send")
#     if month == 1:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="Yes",
#                 PLATE_ENDING="2", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('registration_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration Send")      
#     if month == 2:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="Yes",
#                 PLATE_ENDING="3", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('registration_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration Send")          
#     if month == 3:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="Yes",
#                 PLATE_ENDING="4", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('registration_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration Send")           
#     if month == 4:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="Yes",
#                 PLATE_ENDING="5", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('registration_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration Send")         
#     if month == 5:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="Yes",
#                 PLATE_ENDING="6", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('registration_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration Send")      
#     if month == 6:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="Yes",
#                 PLATE_ENDING="7", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('registration_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration Send")    
#     if month == 7:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="Yes",
#                 PLATE_ENDING="8", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('registration_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration Send")            
#     if month == 8:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="Yes",
#                 PLATE_ENDING="9", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('registration_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration Send")           
#     if month == 9:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="Yes",
#                 PLATE_ENDING="0", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('registration_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration Send")

###########################
######## 2nd Email ########
### Registration and Account Confirmation ####
###########################
# @sched.scheduled_job('interval', minutes=5)
# def reg_email():
#     given_date = datetime.datetime.now().date()
#     sec_week_of_month = given_date.replace(day=15)
#     month = datetime.datetime.now().month
#     year = datetime.datetime.now().year
#     year1 = datetime.datetime.now().year - 1
#     year2 = datetime.datetime.now().year - 2
#     date_now = datetime.datetime.now().date()
#     sent_status = VehicleMasterList.objects.all()
#     if month == 12:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration and Confirmation")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="No",
#                 PLATE_ENDING="1", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('email_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration and Confirmation Send")
#     if month == 1:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration and Confirmation")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="No",
#                 PLATE_ENDING="2", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('email_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration and Confirmation Send")      
#     if month == 2:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration and Confirmation")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="No",
#                 PLATE_ENDING="3", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('email_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration and Confirmation Send")          
#     if month == 3:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration and Confirmation")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="No",
#                 PLATE_ENDING="4", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('email_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration and Confirmation Send")           
#     if month == 4:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration and Confirmation")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="No",
#                 PLATE_ENDING="5", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('email_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration Send")         
#     if month == 5:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration and Confirmation")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="No",
#                 PLATE_ENDING="6", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('email_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration Send")      
#     if month == 6:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration and Confirmation")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="No",
#                 PLATE_ENDING="7", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('email_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration and Confirmation Send")    
#     if month == 7:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration and Confirmation")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="No",
#                 PLATE_ENDING="8", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('email_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration Send")            
#     if month == 8:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration and Confirmation")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="No",
#                 PLATE_ENDING="9", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('email_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration and Confirmation Send")           
#     if month == 9:
#         if sec_week_of_month == given_date:
#             print("2nd Email Registration and Confirmation")
#             exc = Q(ACQ_DATE__year=year) | Q(ACQ_DATE__year=year1) | Q(ACQ_DATE__year=year2)
#             car_status = VehicleMasterList.objects.filter(vehicle_status="Active",smoke="No",confirmation="No",
#                 PLATE_ENDING="0", Status="Yes").exclude(exc)[:80]
#             print(car_status)
#             plate = ""
#             for carreg in car_status:
#                     # print(carreg.plate_no)
#                     plate = carreg.PLATE_NO
#                     print(plate)
#             if car_status != "":
#                 for item in car_status:
#                     data ={
#                         'plate':item.PLATE_NO,
#                         'cs':item.CS_NO,
#                         'cr_name':item.CR_NAME,
#                         'model':item.MODEL,
#                         'brand':item.BRAND,
#                         'make':item.VEHICLE_MAKE,
#                         'type':item.VEHICLE_TYPE,
#                         'lname':item.ASSIGNEE_LAST_NAME,
#                         'fname':item.ASSIGNEE_FIRST_NAME,
#                         'emp_id':item.Employee,
#                         'band':item.BAND_LEVEL,
#                         'cost':item.COST_CENTER,
#                         'group':item.GROUP,
#                         'acq_date':item.ACQ_DATE,
#                         'acq_cost':item.ACQ_COST,
#                     }
#                     subject = 'Reminder for Annual Vehicle Registration - ' + "(" +(item.PLATE_NO) + ")"
#                     html_message = render_to_string('email_template.html',data)
#                     plain_message = item.PLATE_NO
#                     recipient_list = [item.EMAIL]
#                     from_email = 'Fleet Management System <fmsconnected@jxmtsi.com>'
#                     cc_email= ['zscsantos@globe.com.ph','sftaboon@globe.com.ph','zjaperez@globe.com.ph','zsbwarde@globe.com.ph']
#                     toaddrs = recipient_list + cc_email
#                     mail.send_mail(subject, plain_message, from_email, toaddrs, html_message=html_message, fail_silently=False)
#                     print("2nd Email Registration and Confirmation Send")

sched.start()