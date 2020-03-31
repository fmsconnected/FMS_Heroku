from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date,timedelta
from masterlist.models import EmployeeMasterlist,VehicleMasterList
# History
from simple_history.models import HistoricalRecords




							########################################
						   ##########################################
						  #######    CarRental Payment Table  ########
						   ##########################################
						    ########################################


def increment_Activity_id():
	last_in = CarRental.objects.all().order_by('id').last()
	if not last_in:
	    return 'CRP' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'CRP' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

def increment_I_number():
	last_in = CarRental.objects.all().order_by('id').last()
	if not last_in:
	    return 'I' + '000001'
	in_id = last_in.I_number
	in_int = int(in_id[5:])
	new_in_int = in_int + 1
	new_in_id = 'I' + str(new_in_int).zfill(6)
	return new_in_id

class CarRental(models.Model):
	#<-- assignee details---->
	Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	Bill_date = models.CharField(max_length=100, null=True, blank=True)
	Employee_id = models.CharField(max_length=100, null=True, blank=True)
	L_name = models.CharField(max_length=100, null=True, blank=True)
	F_name = models.CharField(max_length=100, null=True, blank=True)
	Assignee_company = models.CharField(max_length=100, null=True, blank=True)
	Cost_center = models.CharField(max_length=100, null=True, blank=True)
	Date_initiated = models.DateField(auto_now=True, blank=True)
	car_provider = models.CharField(max_length=100, null=True, blank=True)
	sqa_number = models.CharField(max_length=100, null=True, blank=True)
	rfp_no2 = models.CharField(max_length=100, null=True, blank=True)
	#<--other assignee---->
	O_Fname = models.CharField(max_length=100, null=True, blank=True)
	O_Lname = models.CharField(max_length=100, null=True, blank=True)
	O_cost_center = models.CharField(max_length=100, null=True, blank=True)
	#<---Vehicle Details-->
	Plate_no = models.CharField(max_length=100, null=True, blank=True)
	V_model = models.CharField(max_length=100, null=True, blank=True)
	V_brand = models.CharField(max_length=100, null=True, blank=True)
	V_make = models.CharField(max_length=100, null=True, blank=True)
	#<---Rental Details--->
	D_vehicle = models.CharField(max_length=100, null=True, blank=True)
	S_rental = models.CharField(max_length=100, null=True, blank=True)
	E_rental = models.CharField(max_length=100, null=True, blank=True)
	R_duration = models.CharField(max_length=100, null=True, blank=True)
	#<---Expense Details--->
	R_Cost = models.CharField(max_length=100, null=True, blank=True)
	G_cost = models.CharField(max_length=100, null=True, blank=True)
	T_fee = models.CharField(max_length=100, null=True, blank=True)
	P_fee = models.CharField(max_length=100, null=True, blank=True)
	Del_fee = models.CharField(max_length=100, null=True, blank=True)
	Dri_fee = models.CharField(max_length=100, null=True, blank=True)
	M_cost = models.CharField(max_length=100, null=True, blank=True)
	O_expenses = models.CharField(max_length=100, null=True, blank=True)
	VAT = models.CharField(max_length=100, null=True, blank=True)
	T_expenses = models.CharField(max_length=100, null=True, blank=True)
	#<-- Other Rental-->
	I_number = models.CharField(max_length=100, null=True, default=increment_I_number)
	I_amount = models.CharField(max_length=100, null=True, blank=True)
	R_purpose = models.CharField(max_length=100, null=True, blank=True)
	C_SLA = models.CharField(max_length=10, null=True, blank=True)
	Deadline = models.DateTimeField()
	history = HistoricalRecords()

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
		return reverse('carrental_list', kwargs={'pk':self.pk})


							########################################
						   ##########################################
						  #######    Vehicle Payment Table    ########
						   ##########################################
						    ########################################


def increment_Activity_id():
	last_in = VehiclePayment.objects.all().order_by('id').last()
	if not last_in:
	    return 'NVP' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[12:])
	new_in_int = in_int + 1
	new_in_id = 'NVP' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id


def increment_PO_no():
	last_in = VehiclePayment.objects.all().order_by('id').last()
	if not last_in:
	    return '000000001'
	in_id = last_in.PO_no
	in_int = int(in_id[5:])
	new_in_int = in_int + 1
	new_in_id = str(new_in_int).zfill(9)
	return new_in_id


class VehiclePayment(models.Model):
	Activity_id = models.CharField(max_length=20, default=increment_Activity_id)
	PO_no = models.CharField(max_length=100, default=increment_PO_no)
	A_employee_ID = models.CharField(max_length=50, null=True, blank=True)
	E_First_name = models.CharField(max_length=50, null=True, blank=True)
	E_Last_name = models.CharField(max_length=50, null=True, blank=True)
	V_deliverDate = models.CharField(max_length=100, null=True,blank=True)
	Plate_no = models.CharField(max_length=20, null=True, blank=True)
	V_model = models.CharField(max_length=100, null=True, blank=True)
	V_brand = models.CharField(max_length=100, null=True, blank=True)
	V_make = models.CharField(max_length=100, null=True, blank=True)
	V_dealer = models.CharField(max_length=100, null=True, blank=True)
	LTO_documents = models.CharField(max_length=100, null=True, blank=True)
	Docs_plate_no = models.CharField(max_length=50, null=True, blank=True)
	LTO_stickers = models.CharField(max_length=100, null=True, blank=True)
	Sticker_fields = models.CharField(max_length=100, null=True, blank=True)
	Date_initial = models.CharField(max_length=100, null=True, blank=True)
	First_payment = models.CharField(max_length=100, null=True, blank=True)
	LTO_charges = models.CharField(max_length=100, null=True, blank=True)
	Outstanding_balance = models.CharField(max_length=100, null=True, blank=True)
	Date_final = models.CharField(max_length=100, null=True, blank=True)
	Routing_remarks = models.CharField(max_length=100, null=True, blank=True)
	V_SLA = models.CharField(max_length=10, null=True, blank=True)
	Next_process = models.CharField(max_length=100, null=True, blank=True)
	Date_initiated = models.DateField(auto_now=True)
	history = HistoricalRecords()
	rfp_number = models.CharField(max_length=100, null=True, blank=True)
	invoice_number = models.CharField(max_length=100, null=True, blank=True)
	equip_no = models.CharField(max_length=100, null=True, blank=True)
	asset_no = models.CharField(max_length=100, null=True, blank=True)
	sap_no = models.CharField(max_length=100, null=True, blank=True)
	mat_no = models.CharField(max_length=100, null=True, blank=True)
	Dealer_name = models.CharField(max_length=100, null=True, blank=True)
	Deadline = models.DateTimeField()	
	# Deadline = models.DateTimeField(default=get_default_Deadline)
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
		return reverse('Vehicle_list')


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

	Activity_id = models.CharField(max_length=20,null=True, default=increment_Activity_id)
	SOA_Date_received = models.CharField(max_length=100, blank=True)
	Fuel_provider = models.CharField(max_length=50, null=True, blank=True)
	SOA_billdate = models.CharField(max_length=100, blank=True)
	SOA_current_amount = models.CharField(max_length=50, null=True, blank=True)
	SOA_outstanding_amount = models.CharField(max_length=50, null=True, blank=True)
	Payee = models.CharField(max_length=10, null=True, choices=PAYEE, blank=True)
	SOA_attached = models.CharField(max_length=100, null=True, blank=True)
	Date_initiated = models.DateField(auto_now=True, blank=True)
	Payment_deadline = models.CharField(max_length=100, blank=True)
	Date_forwarded = models.CharField(max_length=100, blank=True)
	F_SLA = models.CharField(max_length=10, null=True, blank=True)
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

	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('vehiclerepair_payment')




