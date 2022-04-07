from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date,timedelta
from masterlist.models import EmployeeMasterlist
from vehicle_masterlist.models import VehicleMasterList
# History
from simple_history.models import HistoricalRecords



							########################################
						   ##########################################
						  #######    Fuel Supplier Table      ########
						   ##########################################
						    ########################################

def increment_Activity_id():
	last_in = Fuel_supplier.objects.all().order_by('id').last()
	if not last_in:
	    return 'SOA' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'SOA' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id


class Fuel_supplier(models.Model):
	PAYEE = (
		('Globe', 'Globe'),
		('Innove', 'Innove'),
		('Byan', 'Bayan'),
	)

	fuelpro = (
		('SHELL','SHELL'),
		('Petron Corporation','Petron Corporation'),
		('Pilipinas Shell Petroleum Corp.','Pilipinas Shell Petroleum Corp.')
		)
	status=(
		('Ongoing','Ongoing'),
		('Completed','Completed'),
		)
	Activity_id = models.CharField(max_length=20,null=True, default=increment_Activity_id)
	SOA_Date_received = models.CharField(max_length=100,null=True, blank=True)
	Fuel_provider = models.CharField(max_length=50, null=True, blank=True)
	Cost_Center = models.CharField(max_length=100, null=True, blank=True)
	SOA_billdate = models.DateField(auto_now=False,auto_now_add=False,null=True, blank=True)
	SOA_current_amount = models.CharField(max_length=50, null=True, blank=True)
	SOA_outstanding_amount = models.CharField(max_length=50, null=True, blank=True)
	Payee = models.CharField(max_length=10, null=True, choices=PAYEE, blank=True)
	SOA_attached = models.CharField(max_length=100, null=True, blank=True)
	Date_initiated = models.DateField(auto_now=True, null=True, blank=True)
	Date_forwarded = models.CharField(max_length=100, null=True, blank=True)
	F_SLA = models.CharField(max_length=10, null=True, blank=True)
	status = models.CharField(max_length=100, null=True, blank=True, choices=status)
	history = HistoricalRecords()
	Deadline = models.DateTimeField()

	def save(self, *args, **kwargs):
		if self.Deadline is None:
			now = datetime.datetime.today()
			num_days = 0
			while num_days < 15:
				now = now + timedelta(days=1)
				if now.isoweekday() not in [6,7]:
					num_days+=1
			self.Deadline = now
		super().save(*args, **kwargs)

	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('Fuel_supplierList')
