# from django.core.mail import send_mail
# from django.core import mail

# def send_registration_email():
#     month = datetime.datetime.now().month
#     date_now = datetime.datetime.now().date()
#     print(date_now)
#     sent_status = Registration.objects.all()
#     if month == 1:
#         car_status = Registration.objects.filter(
#             Registration_month="JAN", sent_email="No")
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.plate_no)
#                 plate = carreg.PLATE_NO
#                 print(plate)

#         if plate != "":
#             for item in car_status:
#                 subject = 'Fleet Management System Automated Email'
#                 html_message = render_to_string('email.html',{'content':item.PLATE_NO})
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.email]
#                 from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
#                 mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
#                 car_status.update(sent_email="Yes")
#                 car_status.update(Date_email_log= date_now)

#     elif month == 2:
#         car_status = Registration.objects.filter(
#             Registration_month="FEB", sent_email="No")
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.PLATE_NO)
#                 plate = carreg.PLATE_NO
#                 print(plate)

#         if plate != "":
#             for item in car_status:
#                 subject = 'Fleet Management System Automated Email'
#                 html_message = render_to_string('email.html',{'content':item.PLATE_NO})
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.email]
#                 from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
#                 mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
#                 car_status.update(sent_email="Yes")
#                 car_status.update(Date_email_log= date_now)

#     elif month == 3:
#         car_status = Registration.objects.filter(
#             Registration_month="MAR", sent_email="No")
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.PLATE_NO)
#                 plate = carreg.PLATE_NO
#                 print(plate)

#         if plate != "":
#             for item in car_status:
#                 subject = 'Fleet Management System Automated Email'
#                 html_message = render_to_string('email.html',{'content':item.PLATE_NO})
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.email]
#                 from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
#                 mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
#                 car_status.update(sent_email="Yes")
#                 car_status.update(Date_email_log= date_now)

#     elif month == 4:
#         car_status = Registration.objects.filter(
#             Registration_month="APR", sent_email="No")
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.PLATE_NO)
#                 plate = carreg.PLATE_NO
#                 print(plate)

#         if plate != "":
#             for item in car_status:
#                 subject = 'Fleet Management System Automated Email'
#                 html_message = render_to_string('email.html',{'content':item.PLATE_NO})
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.email]
#                 from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
#                 mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
#                 car_status.update(sent_email="Yes")
#                 car_status.update(Date_email_log= date_now)

#     elif month == 5:
#         car_status = Registration.objects.filter(
#             Registration_month="MAY", sent_email="No")
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.PLATE_NO)
#                 plate = carreg.PLATE_NO
#                 print(plate)

#         if plate != "":
#             for item in car_status:
#                 subject = 'Fleet Management System Automated Email'
#                 html_message = render_to_string('email.html',{'content':item.PLATE_NO})
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.email]
#                 from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
#                 mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
#                 car_status.update(sent_email="Yes")
#                 car_status.update(Date_email_log= date_now)

#     elif month == 6:
#         car_status = Registration.objects.filter(
#             Registration_month="JUN", sent_email="No")
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.PLATE_NO)
#                 plate = carreg.PLATE_NO
#                 print(plate)

#         if plate != "":
#             for item in car_status:
#                 subject = 'Fleet Management System Automated Email'
#                 html_message = render_to_string('email.html',{'content':item.PLATE_NO})
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.email]
#                 from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
#                 mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
#                 car_status.update(sent_email="Yes")
#                 car_status.update(Date_email_log= date_now)

#     elif month == 7:
#         car_status = Registration.objects.filter(
#             Registration_month="JUL", sent_email="No")
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.PLATE_NO)
#                 plate = carreg.PLATE_NO
#                 print(plate)

#         if plate != "":
#             for item in car_status:
#                 subject = 'Fleet Management System Automated Email'
#                 html_message = render_to_string('email.html',{'content':item.PLATE_NO})
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.email]
#                 from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
#                 mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
#                 car_status.update(sent_email="Yes")
#                 car_status.update(Date_email_log= date_now)

#     elif month == 8:
#         car_status = Registration.objects.filter(
#             Registration_month="AUG", sent_email="No")
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.PLATE_NO)
#                 plate = carreg.PLATE_NO
#                 print(plate)

#         if plate != "":
#             for item in car_status:
#                 subject = 'Fleet Management System Automated Email'
#                 html_message = render_to_string('email.html',{'content':item.PLATE_NO})
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.email]
#                 from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
#                 mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
#                 car_status.update(sent_email="Yes")
#                 car_status.update(Date_email_log= date_now)

#     elif month == 9:
#         car_status = Registration.objects.filter(
#             Registration_month="SEP", sent_email="No")
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.PLATE_NO)
#                 plate = carreg.PLATE_NO
#                 print(plate)

#         if plate != "":
#             for item in car_status:
#                 subject = 'Fleet Management System Automated Email'
#                 html_message = render_to_string('email.html',{'content':item.PLATE_NO})
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.email]
#                 from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
#                 mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
#                 car_status.update(sent_email="Yes")
#                 car_status.update(Date_email_log= date_now)

#     elif month == 0:
#         car_status = Registration.objects.filter(
#             Registration_month="OCT", sent_email="No")
#         plate = ""
#         for carreg in car_status:
#                 # print(carreg.PLATE_NO)
#                 plate = carreg.PLATE_NO
#                 print(plate)

#         if plate != "":
#             for item in car_status:
#                 subject = 'Fleet Management System Automated Email'
#                 html_message = render_to_string('email.html',{'content':item.PLATE_NO})
#                 plain_message = item.PLATE_NO
#                 recipient_list = [item.email]
#                 from_email = 'Fleet Management System <jxmtsi.fms@gmail.com>'
#                 mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
#                 car_status.update(sent_email="Yes")
#                 car_status.update(Date_email_log= date_now)

