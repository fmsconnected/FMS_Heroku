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

