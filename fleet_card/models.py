from django.db import models
# from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date
from django.db.models import DateTimeField

def increment_Activity_id():
    last_in = fleet_card.objects.all().order_by('id').last()
    if not last_in:
        return 'FCM' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
    in_id = last_in.Activity_id
    in_int = int(in_id[10:])
    new_in_int = in_int + 1
    new_in_id = 'FCM' + str(datetime.datetime.today().strftime('%Y')) + \
        '-' + str(new_in_int).zfill(6)
    return new_in_id


class fleet_card(models.Model):

	station= (
			('PETRON','PETRON'),
			('SHELL','SHELL'),
			('METRO OIL','METRO OIL'),
			('UNIOIL','UNIOIL'),
			('PHOENIX','PHOENIX'),
			('PTT','PTT'),
			('CLEAN FUEL','CLEAN FUEL'),
			('CALTEX','CALTEX'),
			('SEA OIL','SEA OIL'),
		)

	card_type = (
		('VEHICLE CARD','VEHICLE CARD'),
		('DUAL CARD','DUAL CARD'),
		('SINGLE CARD','SINGLE CARD'),
		('DRIVERS CARD','DRIVERS CARD'),
		)
	status = (
		('Ongoing','Ongoing'),
		('Completed','Completed'),
		)
	Activity_id = models.CharField(
	max_length=100, default=increment_Activity_id)
	STATUS = models.CharField(max_length=100, blank=True, null=True, choices=status)
	RECEIVED_REQUEST = models.CharField(max_length=100, blank=True, null=True)
	DATE_VERIFIED = models.CharField(max_length=100, blank=True, null=True)
	DATE_RECEIVED = models.CharField(max_length=100, blank=True, null=True)
	DATE_ISSUED = models.CharField(
	max_length=100, blank=True, null=True)
	WORK_DAYS = models.CharField(max_length=100, blank=True, null=True)
	CARD_NUMBER = models.CharField(
	max_length=254, blank=True, null=True)
	NAME = models.CharField(max_length=254, blank=True, null=True)
	COST_CENTER = models.CharField(max_length=254, blank=True, null=True)
	PLATE_NUMBER = models.CharField(max_length=254, blank=True, null=True)
	CARD_TYPE = models.CharField(max_length=100, blank=True, null=True,choices=card_type)
	CABONILLA = models.CharField(max_length=100, blank=True, null=True)
	STATION = models.CharField(max_length=254, blank=True, null=True,choices=station)
	CRF_NUMBER= models.CharField(max_length=254, blank=True, null=True)
	DATE_OF_CRF_RECEIVED= models.CharField(max_length=254, blank=True, null=True)
	REMARKS= models.CharField(max_length=254, blank=True, null=True)


	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('Fcm_list')


