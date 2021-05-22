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
	last_in = CarRentalRequest.objects.all().order_by('id').last()
	if not last_in:
	    return 'CRR' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'CRR' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id


class CarRentalRequest(models.Model):

	CHOICES= (
		('Ser Roy DelaCruz', 'Ser Roy DelaCruz'),
		('Adolfo Carlos Umali', 'Adolfo Carlos Umali'),
		)
	Rental= (
		('Daily', 'Daily'),
		('Monthly', 'Monthly'),
		)
	Vtype= (
		('Sedan', 'Sedan'),
		('SUV', 'SUV'),
		('VAN', 'VAN'),
	)

	Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	A_Employee = models.CharField(max_length=100, null=True, blank=True)
	Date_received = models.CharField(max_length=100, null=True, blank=True)
	Assignee_Fname = models.CharField(max_length=100, null=True, blank=True)
	Assignee_Lname = models.CharField(max_length=100, null=True, blank=True)
	Assignee_No = models.CharField(max_length=50, null=True, blank=True)
	Assignee_Company = models.CharField(max_length=200, null=True, blank=True)
	Assignee_band = models.CharField(max_length=100,null=True, blank=True)
	Assignee_Dept =models.CharField(max_length=100, null=True, blank=True)
	Assignee_Cost = models.CharField(max_length=100, null=True, blank=True)
	Assignee_Div = models.CharField(max_length=100, null=True, blank=True)
	Assignee_Loc = models.CharField(max_length=200, null=True, blank=True)
	Assignee_Section = models.CharField(max_length=100, null=True, blank=True)
	Assignee_Designation = models.CharField(max_length=100, null=True, blank=True)
	Assignee_ATD = models.CharField(max_length=100, null=True, blank=True)
	Vendor_name = models.CharField(max_length=100, null=True, blank=True)
	Date = models.CharField(max_length=100, null=True, blank=True)
	Up_to = models.CharField(max_length=100, null=True, blank=True)
	Time = models.CharField(max_length=100, null=True, blank=True)
	Place_of_del = models.CharField(max_length=100, null=True, blank=True)
	type_rental = models.CharField(max_length=50, null=True, choices=Rental, blank=True)
	Cost_center = models.CharField(max_length=100, null=True, blank=True)
	Rental_period = models.CharField(max_length=100, null=True, blank=True)
	Destination = models.CharField(max_length=100, null=True, blank=True)
	Delivery_date = models.CharField(max_length=100, null=True, blank=True)
	End_user = models.CharField(max_length=100, null=True, blank=True)
	Type_of_vehicle = models.CharField(max_length=50, null=True, choices=Vtype, blank=True)
	Plate_no = models.CharField(max_length=50, null=True, blank=True)
	Immediate_supervisor = models.CharField(max_length=50, null=True, choices=CHOICES, blank=True)
	CR_SLA = models.CharField(max_length=10, null=True, blank=True)
	Date_initiated = models.DateField(auto_now=True, blank=True)
	history = HistoricalRecords()
	Deadline = models.DateTimeField()

	def save(self, *args, **kwargs):
		if self.Deadline is None:
			now = datetime.datetime.today()
			num_days = 0
			while num_days < 2:
				now = now + timedelta(days=1)
				if now.isoweekday() not in [6,7]:
					num_days+=1
			self.Deadline = now
		super().save(*args, **kwargs)

	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('carrequest_list')

def increment_Activity_id():
	last_in = Gas_card.objects.all().order_by('id').last()
	if not last_in:
		return 'GCR' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'GCR' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

class Gas_card(models.Model):
	card_type= (
		('Single', 'Single'),
		('Driver','Driver'),
		('Vehicle','Vehicle'),
	)
	fleet_card= (
		('Petron', 'Petron'),
		('Shell','Shell'),
	)
	app_type= (
		('Daily', 'Daily'),
		('Transfer Acountability', 'Transfer Acountability'),
		('Cancel - Disposal of Vehicle', 'Cancel - Disposal of Vehicle'),
		('Cancel - Resignation of User', 'Cancel - Resignation of User'),
		('Replacement - Damage', 'Replacement - Damage'),
		('Replacement - Lose', 'Replacement - Lose'),
		('Others - Adjust Credit Limit', 'Others - Adjust Credit Limit'),
		('Others - Change of Product Restriction', 'Others - Change of Product Restriction'),
		('Others - Update Cost Center', 'Others - Update Cost Center'),
	)
	restrictions= (
		('S: Super Only', 'S: Super Only'),
		('U: Super Unleaded Only', 'U: Super Unleaded Only'),
		('R: Regular Only', 'R: Regular Only'),
		('X: Velocity', 'X: Velocity'),
		('D: Diesoline Only', 'D: Diesoline Only'),
		('L: Lubricant Only', 'L: Lubricant Only'),
		('V: Service Only', 'V: Service Only'),
		('C: Convenience store items, sundries, accesories', 'C: Convenience store items, sundries, accesories'),
	)
	approved= (
		('Ser Roy Perluval Dela Cruz','Ser Roy Perluval Dela Cruz'),
	)

	cancellation= (
		('Disposal Of Vehicle','Disposal Of Vehicle'),
		('Resignation of User','Resignation of User'),
	)

	Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	date_received = models.CharField(max_length=100, null=True, blank=True)
	application_type = models.CharField(max_length=100, null=True, blank=True, choices=app_type)
	fleet_provider= models.CharField(max_length=100, null=True, choices=fleet_card, blank=True)
	fleetcard_type = models.CharField(max_length=100, null=True, choices=card_type, blank=True)
	fuel_limit_amount = models.CharField(max_length=100, null=True, blank=True)
	fuel_limit_quantity = models.CharField(max_length=100, null=True, blank=True)
	products_restriction = models.CharField(max_length=100, null=True, choices=restrictions, blank=True)
	req_employee = models.CharField(max_length=100, null=True, blank=True)
	req_fname = models.CharField(max_length=100, null=True, blank=True)
	req_lname = models.CharField(max_length=100, null=True, blank=True)
	req_title = models.CharField(max_length=100, null=True, blank=True)
	req_cost_center = models.CharField(max_length=100, null=True, blank=True)
	atd_no = models.CharField(max_length=100, null=True, blank=True)
	temporary_atd = models.CharField(max_length=100, null=True, blank=True)
	new_emp_id = models.CharField(max_length=100, null=True, blank=True)
	new_emp_fname = models.CharField(max_length=100, null=True, blank=True)
	new_emp_lname = models.CharField(max_length=100, null=True, blank=True)
	new_emp_cost = models.CharField(max_length=100, null=True, blank=True)
	new_temp_atd = models.CharField(max_length=100, null=True, blank=True)
	new_assignee = models.CharField(max_length=100, null=True, blank=True)
	cost_center_code = models.CharField(max_length=100, null=True, blank=True)
	cancellation = models.CharField(max_length=100, null=True, choices=cancellation, blank=True)
	plate_no = models.CharField(max_length=100, null=True, blank=True)
	con_sticker = models.CharField(max_length=100, null=True, blank=True)
	model_year = models.CharField(max_length=100, null=True, blank=True)
	brand = models.CharField(max_length=100, null=True, blank=True)
	make = models.CharField(max_length=100, null=True, blank=True)
	fuel_type = models.CharField(max_length=100, null=True, blank=True)
	new_plate_no = models.CharField(max_length=100, null=True, blank=True)
	new_cond_sticker = models.CharField(max_length=100, null=True, blank=True)
	new_model_year = models.CharField(max_length=100, null=True, blank=True)
	new_vbrand = models.CharField(max_length=100, null=True, blank=True)
	new_vmake = models.CharField(max_length=100, null=True, blank=True)
	new_vfuel_type = models.CharField(max_length=100, null=True, blank=True)
	approved_by = models.CharField(max_length=100, null=True, choices=approved, blank=True)
	date_summitted =models.CharField(max_length=100, null=True, blank=True)
	fleet_received = models.CharField(max_length=100, null=True, blank=True)
	fleet_card_no = models.CharField(max_length=100, null=True, blank=True)
	fleet_date_release = models.CharField(max_length=100, null=True, blank=True)
	person_release = models.CharField(max_length=100, null=True, blank=True)
	date_initiated = models.DateField(auto_now=True, blank=True)
	GCR_SLA = models.CharField(max_length=20, null=True, blank=True)
	history = HistoricalRecords()
	Deadline = models.DateTimeField()

	def save(self, *args, **kwargs):
		if self.Deadline is None:
			now = datetime.datetime.today()
			num_days = 0
			while num_days < 10:
				now = now + timedelta(days=1)
				if now.isoweekday() not in [6,7]:
					num_days+=1
			self.Deadline = now
		super().save(*args, **kwargs)

	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('gascard_list')

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


def increment_Activity_id():
	last_in = Vehicle_Repair.objects.all().order_by('id').last()
	if not last_in:
		return 'VRR' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'VRR' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

class Vehicle_Repair(models.Model):
	area= (
		('The Globe Tower', 'The Globe Tower'),
		('Visayas-Mindanao', 'Visayas-Mindanao'),
	)
	
	verified= (
		('Shane Santos','Shane Santos'),
	)
	# shop= (
	# 	('GR8','GR8'),
	# 	('Others','Others')
	# )
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
			('Yes', 'Yes'),
			('No', 'No'),
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
	VRR_SLA = models.CharField(max_length=10, null=True, blank=True)
	email = models.CharField(max_length=100,null=True,blank=True)
	date_initiated = models.DateField(auto_now=True, null=True, blank=True)
	sent_email = models.CharField(max_length=10, null=True, blank=True,choices=status)
	Date_email_log = models.CharField(max_length=20, null=True, blank=True)
	history = HistoricalRecords()
	Deadline = models.DateTimeField()

	def save(self, *args, **kwargs):
		if self.Deadline is None:
			now = datetime.datetime.today()
			num_days = 0
			while num_days < 30:
				now = now + timedelta(days=1)
				if now.isoweekday() not in [7]:
					num_days+=1
			self.Deadline = now
		super().save(*args, **kwargs)

	def __str__(self):
		return self.plate_no

	def get_absolute_url(self):
		return reverse('repair_list')
		
# class Vehicle_Repair_email(models.Model):
# 	status = (
# 			('Yes', 'Yes'),
# 			('No', 'No'),
# 		)

# 	Plate_no = models.CharField(max_length=100, null=True, blank=True)
# 	email = models.CharField(max_length=100,null=True,blank=True)
# 	sent_email = models.CharField(max_length=10, null=True, blank=True,choices=status)
# 	Deadline = models.DateTimeField()

# 	def save(self, *args, **kwargs):
# 		if self.Deadline is None:
# 			now = datetime.datetime.today()
# 			num_days = 0
# 			while num_days < 30:
# 				now = now + timedelta(days=1)
# 				if now.isoweekday() not in [7]:
# 					num_days+=1
# 			self.Deadline = now
# 		super().save(*args, **kwargs)

# 	def __str__(self):
# 		return self.email

# 	def get_absolute_url(self):
# 		return reverse('repair_list')