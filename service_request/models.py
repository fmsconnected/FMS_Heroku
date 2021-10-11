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
	last_in = service_vehicle.objects.all().order_by('id').last()
	if not last_in:
		return 'SVV' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'SVV' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id		

class service_vehicle(models.Model):
	vtype= (
		('Sedan', 'Sedan'),
		('SUV', 'SUV '),
		('Pick up 4x2', 'Pick up 4x2'),
		('Pick Up 4x4', 'Pick Up 4x4'),
		('AUV', 'AUV'),
		('Others', 'Others '),
	)
	approvedby= (
		('Ser Roy Dela Cruz', 'Ser Roy Dela Cruz'),
		('Adolfo Carlos Umali', 'Adolfo Carlos Umali '),
	)
	vprovider= (
		('Orix', 'Orix'),
		('Diamond', 'Diamond '),
		('Safari', 'Safari'),
	)
	vbrand= (
		('BMW', 'BMW'),
		('Chevrolet', 'Chevrolet '),
		('chrysler', 'chrysler'),
		('Ford', 'Ford'),
		('Honda', 'Honda '),
		('Hyundai', 'Hyundai'),
		('Isuzu', 'Isuzu'),
		('Kia', 'Kia '),
		('Masda', 'Masda'),
		('Mitsubishi', 'Mitsubishi'),
		('Nissan', 'Nissan '),
		('Peugeot', 'Peugeot'),
		('Subaro', 'Subaro'),
	)
	status = (
		("Ongoing","Ongoing"),
		("Completed","Completed"),
		)
	
	Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	request_date = models.CharField(max_length=100, null=True, blank=True)
	req_employee_id = models.CharField(max_length=100, null=True, blank=True)
	req_lname = models.CharField(max_length=100, null=True, blank=True)
	req_fname = models.CharField(max_length=100, null=True, blank=True)
	assignee_employee_id = models.CharField(max_length=100, null=True, blank=True)
	assignee_group = models.CharField(max_length=100, null=True, blank=True)
	assignee_fname = models.CharField(max_length=100, null=True, blank=True)
	assignee_lname = models.CharField(max_length=100, null=True, blank=True)
	assignee_costcenter = models.CharField(max_length=100, null=True, blank=True)
	assignee_section = models.CharField(max_length=100, null=True, blank=True)
	assignee_location = models.CharField(max_length=100, null=True, blank=True)
	assignee_atd = models.CharField(max_length=100, null=True, blank=True)
	new_employee_id = models.CharField(max_length=100, null=True, blank=True)
	new_employee_fname = models.CharField(max_length=100, null=True, blank=True)
	new_employee_lname = models.CharField(max_length=100, null=True, blank=True)
	new_employee_cost = models.CharField(max_length=100, null=True, blank=True)
	new_temporary_atd = models.CharField(max_length=100, null=True, blank=True)
	prefered_vehicle = models.CharField(max_length=100, null=True, choices=vtype, blank=True)
	justification = models.CharField(max_length=100, null=True, blank=True)
	E_plate_no = models.CharField(max_length=100, null=True, blank=True)
	E_con_sticker = models.CharField(max_length=100, null=True, blank=True)
	E_model_year = models.CharField(max_length=100, null=True, blank=True)
	E_brand = models.CharField(max_length=100, null=True, blank=True)
	E_make = models.CharField(max_length=100, null=True, blank=True)
	E_type = models.CharField(max_length=100, null=True, blank=True)
	approved_by = models.CharField(max_length=100, null=True, choices=approvedby, blank=True)
	approved_date = models.CharField(max_length=100, null=True, blank=True)
	vehicle_provider = models.CharField(max_length=100, null=True, choices=vprovider, blank=True)
	vehicle_plate_no = models.CharField(max_length=100, null=True, blank=True)
	vehicle_CS_no = models.CharField(max_length=100, null=True, blank=True)
	vehicle_model = models.CharField(max_length=100, null=True, blank=True)
	vehicle_brand = models.CharField(max_length=100, null=True, choices=vbrand, blank=True)
	vehicle_make = models.CharField(max_length=100, null=True, blank=True)
	vehicle_fuel_type = models.CharField(max_length=100, null=True, blank=True)
	SVV_SLA = models.CharField(max_length=10, null=True, blank=True)
	date_initiated = models.DateField(auto_now=True, null=True)
	history = HistoricalRecords()
	Status = models.CharField(max_length=200, null=True, blank=True, choices=status)
	Deadline = models.DateTimeField(auto_now=False, null=True, blank=True)

	# def save(self, *args, **kwargs):
	# 	if self.Deadline is None:
	# 		now = datetime.datetime.today()
	# 		num_days = 0
	# 		while num_days < 60:
	# 			now = now + timedelta(days=1)
	# 			if now.isoweekday() not in [6,7]:
	# 				num_days+=1
	# 		self.Deadline = now
	# 	super().save(*args, **kwargs)


	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('service_list')

