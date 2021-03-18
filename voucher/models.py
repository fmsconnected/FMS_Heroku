from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date
from masterlist.models import EmployeeMasterlist
from vehicle_masterlist.models import VehicleMasterList
# History
from simple_history.models import HistoricalRecords

def increment_Activity_id():
	last_in = expense_voucher.objects.all().order_by('id').last()
	if not last_in:
		return 'EVO' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'EVO' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

class expense_voucher(models.Model):
	fleet_area= (
		('The Globe Tower','The Globe Tower'),
		('Visayas-Mindanao','Visayas-Mindanao'),
	)
	trans= (
		('Gas Reimbursements','Gas Reimbursements'),
		('Car Parts Replacement','Car Parts Replacement'),
		('GR and CPR','GR and CPR'),
	)
	voucher_type= (
		('Expense Voucher','Expense Voucher'),
		('Petty Cash Voucher','Petty Cash Voucher'),
		('EV and PCV','EV and PCV'),
	)
	brand= (
		('BMW','BMW'),
		('Chevrolet','Chevrolet'),
		('Chrysler','Chrysler'),
		('Ford','Ford'),
		('Honda','Honda'),
		('Hyundai','Hyundai'),
		('Isuzu','Isuzu'),
		('Kia','Kia'),
		('Masda','Masda'),
		('Mitsubishi','Mitsubishi'),
		('Nissan','Nissan'),
		('Peugeot','Peugeot'),
		('Subaro','Subaro'),
	)
	sup= (
		('Ser Roy Dela Cruz','Ser Roy Dela Cruz'),
		('Adolfo Carlos Umali','Adolfo Carlos Umali'),
	)
	admin= (
		('Approved','Approved'),
	)
	Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	# employee_id = models.ForeignKey('masterlist.EmployeeMasterlist', on_delete=models.DO_NOTHING)
	employee_id = models.CharField(max_length=100, blank=True, null=True)
	employee_fname = models.CharField(max_length=100, blank=True, null=True)
	employee_lname = models.CharField(max_length=100, blank=True, null=True)
	employee_group = models.CharField(max_length=100, blank=True, null=True)
	employee_cost = models.CharField(max_length=100, blank=True, null=True)
	new_employee_id = models.CharField(max_length=100, blank=True, null=True)
	new_employee_fname = models.CharField(max_length=100, blank=True, null=True)
	new_employee_lname = models.CharField(max_length=100, blank=True, null=True)
	new_employee_group = models.CharField(max_length=100, blank=True, null=True)
	new_employee_cost = models.CharField(max_length=100, blank=True, null=True)
	fleet_area = models.CharField(max_length=100, null=True, blank=True, choices=fleet_area)
	received_voucher = models.CharField(max_length=100, blank=True, null=True)
	trans_type = models.CharField(max_length=100, blank=True, null=True, choices=trans)
	voucher_no = models.CharField(max_length=100, blank=True, null=True)
	voucher_amount = models.CharField(max_length=100, blank=True, null=True)
	voucher_type = models.CharField(max_length=100, blank=True, null=True, choices=voucher_type)
	fuel_amount = models.CharField(max_length=100, blank=True, null=True)
	fuel_products = models.CharField(max_length=100, blank=True, null=True)
	fuel_liters = models.CharField(max_length=100, blank=True, null=True)
	service_amount = models.CharField(max_length=100, blank=True, null=True)
	work_order = models.CharField(max_length=100, blank=True, null=True)
	# plate_number = models.ForeignKey('masterlist.VehicleMasterList', on_delete=models.DO_NOTHING)
	plate_number = models.CharField(max_length=100, blank=True, null=True)
	odometer_start = models.CharField(max_length=100, blank=True, null=True)
	odometer_end = models.CharField(max_length=100, blank=True, null=True)
	v_brand = models.CharField(max_length=100, blank=True, null=True, choices=brand)
	v_make = models.CharField(max_length=100, blank=True, null=True)
	v_fuel_type = models.CharField(max_length=100, blank=True, null=True)
	v_model = models.CharField(max_length=100, blank=True, null=True)
	new_plate_number = models.CharField(max_length=100, blank=True, null=True)
	new_odometer_start = models.CharField(max_length=100, blank=True, null=True)
	new_odometer_end = models.CharField(max_length=100, blank=True, null=True)
	new_v_brand = models.CharField(max_length=100, blank=True, null=True, choices=brand)
	new_v_make = models.CharField(max_length=100, blank=True, null=True)
	new_v_fuel_type = models.CharField(max_length=100, blank=True, null=True)
	new_v_model = models.CharField(max_length=100, blank=True, null=True)
	gt_admin = models.CharField(max_length=100, blank=True, null=True, choices=admin)
	approval_date = models.CharField(max_length=100, blank=True, null=True)
	immediate_supervisor = models.CharField(max_length=100, blank=True, null=True, choices=sup)
	im_approval_date = models.CharField(max_length=100, blank=True, null=True)
	voucher_docs1 = models.CharField(max_length=100, blank=True, null=True)
	voucher_docs2 = models.CharField(max_length=100, blank=True, null=True)
	voucher_docs3 = models.CharField(max_length=100, blank=True, null=True)
	voucher_remarks = models.CharField(max_length=100, blank=True, null=True)
	voucher_forwarded = models.CharField(max_length=100, blank=True, null=True)
	EVO_SLA = models.CharField(max_length=10, null=True)
	date_initiated = models.DateField(auto_now=True, null=True)
	history = HistoricalRecords()

	def __str__(self):
    		return self.Activity_id

	def get_absolute_url(self):
		return reverse('voucher_list')
    