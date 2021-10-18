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
	status = (
			('Ongoing', 'Ongoing'),
			('Completed', 'Completed'),
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
	status = models.CharField(max_length=100, null=True, blank=True, choices=status)
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

