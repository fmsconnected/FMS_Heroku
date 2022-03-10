from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date
from dateutil import tz

# History
from simple_history.models import HistoricalRecords


def increment_Activity_Id():
	last_in = VehicleMasterList.objects.all().order_by('id').last()
	if not last_in:
	    return 'VML' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_Id
	in_int = int(in_id[8:])
	new_in_int = in_int + 1
	new_in_id = 'VML' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

def increment_NO():
	last_in = VehicleMasterList.objects.all().order_by('id').last()
	if not last_in:
	    return '000001'
	in_id = last_in.NO
	in_int = int(in_id[0:])
	new_in_int = in_int + 1
	new_in_id = str(new_in_int).zfill(6)
	return new_in_id


class VehicleMasterList(models.Model):
	Vbrand= (
			('Honda','Honda'),
			('Toyota','Toyota'),
			('Mitsubishi','Mitsubishi'),
			('Ford','Ford'),
			('Masda','Masda'),
			('Isuzu','Isuzu'),
			('Hyundai','Hyundai'),
			('Nissan','Nissan'),
			('SuZuki','Suzuki'),
			('Chevrolet','Chevrolet'),
			('Audi','Audi'),
			('BMW','BMW'),
			('Bently','Bently'),
			('Cadillac','Cadillac'),
			('Chrysler','Chrysler'),
			('Dodge','Dodge'),
			('GMC','GMC'),
			('Genesis','Genesis'),
			('Jaguar','Jaguar'),
			('Land Rover','Land Rover'),
			('Lexus','Lexus'),
			('Lincoln','Lincoln'),
			('Lotus','Lotus'),
			('Maserati','Maserati'),
			('Mercedes-Benz','Mercedes-Benz'),
			('Mini','Mini'),
			('Porsche','Porsche'),
			('Ram','Ram'),
			('Rolls-Royce','Rolls-Royce'),
			('Saab','Saab'),
			('Scion','Scion'),
			('Subaru','Subaru'),
			('Tesla','Tesla'),
			('Volkswagen','Volkswagen'),
			('Volvo','Volvo'),
			('Saturn','Saturn'),
			('Kia','Kia'),
			('Geely','Geely'),
			('MG','MG')
            )
	remarks = (
            ('Ongoing', 'Ongoing'),
            ('Complete','Complete'),
            )

	status = (
			('Yes', 'Yes'),
			('No', 'No'),
		)
	email = (
			('Yes', 'Yes'),
			('No', 'No'),
		)
	vstatus = (
			('Sold', 'Sold'),
			('Transferred', 'Transferred'),
			('Active', 'Active'),
		)
	
	Activity_Id  = models.CharField(max_length=100,null=True, default=increment_Activity_Id)
	NO = models.CharField(max_length=100, null=True, default=increment_NO)
	PLATE_NO = models.CharField(max_length=100, null=True, blank=True)
	CS_NO = models.CharField(max_length=100, null=True, blank=True)
	CR_NAME = models.CharField(max_length=100, null=True, blank=True)
	PLATE_ENDING = models.CharField(max_length=1, null=True, blank=True)
	REGISTRATION_MONTH = models.CharField(max_length=5, null=True, blank=True)
	MODEL = models.CharField(max_length=10, null=True, blank=True)
	BRAND = models.CharField(max_length=100, null=True, choices=Vbrand)
	VEHICLE_MAKE = models.CharField(max_length=100, null=True, blank=True)
	ENGINE_NO = models.CharField(max_length=100, null=True, blank=True)
	CHASSIS_NO = models.CharField(max_length=100, null=True, blank=True)
	MV_FILE_NO = models.CharField(max_length=100, null=True, blank=True)
	VEHICLE_TYPE = models.CharField(max_length=100, null=True, blank=True)
	Employee = models.CharField(max_length=100, null=True,blank=True)
	# Employee = models.ForeignKey(EmployeeMasterlist, default=None,null=True,blank=True, on_delete=models.SET_NULL)
	ASSIGNEE_LAST_NAME = models.CharField(max_length=100, null=True, blank=True)
	ASSIGNEE_FIRST_NAME = models.CharField(max_length=100, null=True, blank=True)
	VEHICLE_CATEGORY = models.CharField(max_length=100, null=True, blank=True)
	BAND_LEVEL  = models.CharField(max_length=100, null=True, blank=True)
	BENEFIT_GROUP = models.CharField(max_length=100, null=True, blank=True)
	COST_CENTER = models.CharField(max_length=100, null=True, blank=True)
	GROUP = models.CharField(max_length=100, null=True, blank=True)
	DIVISION = models.CharField(max_length=100, null=True, blank=True)
	DEPARTMENT = models.CharField(max_length=100, null=True, blank=True)
	SECTION = models.CharField(max_length=100, null=True, blank=True)
	IS_ID = models.CharField(max_length=100, null=True, blank=True)
	IS_NAME = models.CharField(max_length=100, null=True, blank=True)
	LOCATION = models.CharField(max_length=100, null=True, blank=True)
	AREA = models.CharField(max_length=254, null=True, blank=True)
	EMAIL = models.CharField(max_length=254, null=True, blank=True)
	ORIGINAL_OR_DATE  = models.DateField(auto_now=False,auto_now_add=False, null=True, blank=True,default=None)
	ACQ_DATE  = models.DateField(auto_now=False, null=True, blank=True)
	ACQ_COST = models.CharField(max_length=100, null=True, blank=True)
	ASSET_NO = models.CharField(max_length=100, null=True, blank=True)
	EQUIPMENT_NO = models.CharField(max_length=100, null=True, blank=True)
	SAP_PR = models.CharField(max_length=100, null=True, blank=True)
	Vehicle_IVN_no = models.CharField(max_length=100, null=True, blank=True)
	Unit_MATDOC = models.CharField(max_length=100, null=True, blank=True)
	dealer = models.CharField(max_length=100, null=True, blank=True)
	dealer_name = models.CharField(max_length=100, null=True, blank=True)
	PO_NO = models.CharField(max_length=100, null=True, blank=True)
	CHECKLIST_BY = models.CharField(max_length=254, null=True, blank=True)
	PLATE_NUMBER_RELEASE_DATE = models.DateField(auto_now=False,auto_now_add=False, null=True, blank=True,default=None)
	Last_Registration_Date = models.CharField(max_length=100, null=True, blank=True,default=None)
	Smoke_Emission_Date = models.CharField(max_length=100, null=True, blank=True, choices=status)
	Smoke_due = models.DateField(auto_now=False, null=True, blank=True)
	COC_Date = models.CharField(max_length=100, null=True, blank=True,choices=status)
	Remarks = models.CharField(max_length=250, null=True, blank=True, choices=remarks)
	Status = models.CharField(max_length=20, null=True, blank=True)
	leasing_remark = models.CharField(max_length=225, null=True, blank=True)
	vehicle_status = models.CharField(max_length=100, null=True, blank=True, choices=vstatus)
	Status_2 = models.CharField(max_length=10, null=True, blank=True)
	Status_3 = models.CharField(max_length=10, null=True, blank=True)
	Status_4 = models.CharField(max_length=10, null=True, blank=True)
	confirmation = models.CharField(max_length=10, null=True, blank=True, choices=email)
	smoke = models.CharField(max_length=10, null=True, blank=True, choices=email)
	Date_email_log = models.CharField(max_length=20, null=True, blank=True)
	history = HistoricalRecords()

	def __str__(self):
		return self.PLATE_NO
		# return str(self.id)
	def get_absolute_url(self):
		return reverse('vehicle-list')



