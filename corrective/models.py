from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date,timedelta
from masterlist.models import EmployeeMasterlist
from vehicle_masterlist.models import VehicleMasterList
# History
from simple_history.models import HistoricalRecords

def increment_Activity_id():
	last_in = Corrective.objects.all().order_by('id').last()
	if not last_in:
		return 'VRR' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'VRR' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id
	
class Corrective(models.Model):
	area= (
		('The Globe Tower', 'The Globe Tower'),
		('Visayas-Mindanao', 'Visayas-Mindanao'),
	)
	
	verified= (
		('Shane Santos','Shane Santos'),
	)
	maintenance= (
		('Preventive Maintenance','Preventive Maintenance'),
		('Corective Maitenance','Corective Maitenance'),
		('Battery','Battery'),
		('Tire','Tire'),
	)
	approvedby= (
		('Ser Roy Perluval Dela Cruz','Ser Roy Perluval Dela Cruz'),
		('Adolfo Carlos Umali','Adolfo Carlos Umali'),
	)
	status = (
		("Ongoing","Ongoing"),
		("Completed","Completed"),
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
	fleet_area = models.CharField(max_length=100, null=True, choices=area, blank=True)
	particulars = models.CharField(max_length=100, null=True, blank=True)
	category = models.CharField(max_length=100, null=True, blank=True)
	maintenance_type1 = models.CharField(max_length=100, null=True, choices=maintenance, blank=True)
	scope_work1 = models.CharField(max_length=100, null=True, blank=True)
	maintenance_type2 = models.CharField(max_length=100, null=True, blank=True, choices=maintenance)
	scope_work2 = models.CharField(max_length=100, null=True, blank=True)
	recommendations = models.CharField(max_length=100, null=True, blank=True)
	service_reminder = models.CharField(max_length=100, null=True, blank=True)
	verified_by = models.CharField(max_length=100, null=True, blank=True, choices=verified)
	work_order1 = models.CharField(max_length=100, null=True, blank=True)
	work_order2 = models.CharField(max_length=100, null=True, blank=True)
	work_order3 = models.CharField(max_length=100, null=True, blank=True)
	datework_created = models.CharField(max_length=100, null=True, blank=True)
	Shop_vendor = models.CharField(max_length=100, null=True, blank=True)
	memo_app = models.CharField(max_length=100, null=True, blank=True)
	date_forwarded = models.CharField(max_length=100, null=True, blank=True)
	estimate_no = models.CharField(max_length=100, null=True, blank=True)
	maintenance_amount = models.CharField(max_length=100, null=True, blank=True)
	less_discount = models.CharField(max_length=100, null=True, blank=True)
	estimate_remarks = models.CharField(max_length=100, null=True, blank=True)
	estimate_attached = models.CharField(max_length=100, null=True, blank=True)
	approvedby = models.CharField(max_length=100, null=True, choices=approvedby, blank=True)
	meter_reading = models.CharField(max_length=100, null=True, blank=True)
	date_initiated = models.DateField(auto_now=True, null=True, blank=True)
	status = models.CharField(max_length=100, null=True, blank=True, choices=status)
	history = HistoricalRecords()

	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('corrective_list')

