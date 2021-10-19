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
						  #######    Vehicle Repair Table     ########
						   ##########################################
						    ########################################

def increment_Activity_id():
	last_in = Vehicle_Repair_payment.objects.all().order_by('id').last()
	if not last_in:
		return 'VRP' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'VRP' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

class Vehicle_Repair_payment(models.Model):

	maintenance= (
		('Preventive Maintenance','Preventive Maintenance'),
		('Corective Maitenance','Corective Maitenance'),
		('Battery','Battery'),
		('Tire','Tire'),
		)
	status = (
			('Ongoing', 'Ongoing'),
			('Completed', 'Completed'),
		)
	Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	request_date = models.DateField(auto_now=False, null=True)
	employee = models.CharField(max_length=100, null=True, blank=True)
	cost_center = models.CharField(max_length=100, null=True, blank=True)
	first_name = models.CharField(max_length=100, null=True, blank=True)
	last_name = models.CharField(max_length=100, null=True, blank=True)
	contact_no = models.CharField(max_length=100, null=True, blank=True)
	company = models.CharField(max_length=100, null=True, blank=True)
	department = models.CharField(max_length=100, null=True, blank=True)
	group_section = models.CharField(max_length=100, null=True, blank=True)
	plate_no = models.CharField(max_length=100, null=True, blank=True)
	v_brand = models.CharField(max_length=100, null=True, blank=True)
	engine = models.CharField(max_length=100, null=True, blank=True)
	v_make = models.CharField(max_length=100, null=True, blank=True)
	v_model = models.CharField(max_length=100, null=True, blank=True)
	chassis = models.CharField(max_length=100, null=True, blank=True)
	band = models.CharField(max_length=100, null=True, blank=True)
	cond_sticker = models.CharField(max_length=100, null=True, blank=True)
	equipment_no = models.CharField(max_length=100, null=True, blank=True)
	dealership = models.CharField(max_length=100, null=True, blank=True)
	amount = models.CharField(max_length=20, null=True, blank=True)
	service_type = models.CharField(max_length=100, null=True, blank=True, choices=maintenance)
	date_initiated = models.DateField(auto_now=True)
	history = HistoricalRecords()
	rfp_no = models.CharField(max_length=100, null=100, blank=True)
	invoice_number2 = models.CharField(max_length=100, null=100, blank=True)
	invoice_date = models.CharField(max_length=100, null=100, blank=True)
	Status = models.CharField(max_length=100, null=True, blank=True, choices=status)

	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('vehiclerepair_payment')





