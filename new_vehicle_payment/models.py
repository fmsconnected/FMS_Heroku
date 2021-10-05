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
	status = (
			('Ongoing', 'Ongoing'),
			('Completed', 'Completed'),
		)
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
	Status = models.CharField(max_length=100, null=True, blank=True, choices=status)
	Dealer_name = models.CharField(max_length=100, null=True, blank=True)
	Deadline = models.DateTimeField()	

	def save(self, *args, **kwargs):
		if self.Deadline is None:
			now = datetime.datetime.today()
			num_days = 0
			while num_days < 30:
				now = now + timedelta(days=1)
				if now.isoweekday() not in [6,7]:
					num_days+=1
			self.Deadline = now
		super().save(*args, **kwargs)

	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('Vehicle_list')

