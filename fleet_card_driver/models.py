from django.db import models
# from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date
from django.db.models import DateTimeField

def increment_Activity_id():
    last_in = fleet_card_driver.objects.all().order_by('id').last()
    if not last_in:
        return 'FCD' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
    in_id = last_in.Activity_id
    in_int = int(in_id[10:])
    new_in_int = in_int + 1
    new_in_id = 'FCD' + str(datetime.datetime.today().strftime('%Y')) + \
        '-' + str(new_in_int).zfill(6)
    return new_in_id


class fleet_card_driver(models.Model):

	status = (
		('Ongoing','Ongoing'),
		('Completed','Completed'),
		)
	Activity_id = models.CharField(
	max_length=100, default=increment_Activity_id)
	STATUS = models.CharField(max_length=100, blank=True, null=True, choices=status)
	SOA_DATE = models.CharField(max_length=100, blank=True, null=True)
	SOA_NO = models.CharField(max_length=100, blank=True, null=True)
	AMOUNT = models.CharField(max_length=100, blank=True, null=True)
	COST_CENTER = models.CharField(
	max_length=100, blank=True, null=True)
	DTR_CUTOFF = models.CharField(max_length=100, blank=True, null=True)
	REF_NO = models.CharField(
	max_length=254, blank=True, null=True)
	REMARKS= models.CharField(max_length=254, blank=True, null=True)


	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('FCD_list')


