from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date
# History
from simple_history.models import HistoricalRecords

class EmployeeMasterlist(models.Model):
	Company = models.CharField(max_length=100, null=True)
	Employee_Id = models.CharField(max_length=100, null=True)
	Last_name = models.CharField(max_length=50, null=True)
	First_name = models.CharField(max_length=50, null=True)
	Middle_name = models.CharField(max_length=20, null=True)
	Suffix = models.CharField(max_length=20, null=True)
	Band = models.CharField(max_length=50, null=True)
	Cost_center = models.CharField(max_length=100, null=True)
	DIV_code = models.CharField(max_length=100, null=True)
	Group = models.CharField(max_length=100, null=True)
	Division = models.CharField(max_length=100, null=True)
	Department = models.CharField(max_length=100, null=True)
	Section = models.CharField(max_length=100, null=True)
	Unit = models.CharField(max_length=100, null=True)
	Sub_unit = models.CharField(max_length=100, null=True)
	IS_ID = models.CharField(max_length=100, null=True)
	IS_lastname = models.CharField(max_length=100, null=True)
	IS_firstname = models.CharField(max_length=100, null=True)
	Location = models.CharField(max_length=100, null=True)
	Area = models.CharField(max_length=100, null=True)
	Area2 = models.CharField(max_length=100, null=True)
	Benefit = models.CharField(max_length=100, null=True)
	history = HistoricalRecords()

	def __str__(self):
		return self.Employee_Id
		
	def get_absolute_url(self):
		return reverse('employee-list')

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
            )
	remarks = (
            ('Without Last Registration Date','Without Last Registration Date'),
            ('Without Smoke Emission Date','Without Smoke Emission Date'),
            ('Without COC Date','Without COC Date'),
            ('No Smoke and COC', 'No Smoke and COC'),
            ('For Registration', 'For Registration'),
            ('Complete','Complete'),
            )

	status = (
			('Yes', 'Yes'),
			('Not', 'Not'),
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
	IS_LAST_NAME = models.CharField(max_length=100, null=True, blank=True)
	IS_FIRST_NAME = models.CharField(max_length=100, null=True, blank=True)
	LOCATION = models.CharField(max_length=100, null=True, blank=True)
	ORIGINAL_OR_DATE  = models.DateField(auto_now=False, null=True, blank=True)
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
	PLATE_NUMBER_RELEASE_DATE = models.DateField(auto_now=False, null=True, blank=True)
	Employee = models.CharField(max_length=100, null=True)
	Last_Registration_Date = models.CharField(max_length=100, null=True, blank=True)
	Smoke_Emission_Date = models.CharField(max_length=100, null=True, blank=True)
	COC_Date = models.CharField(max_length=100, null=True, blank=True)
	Remarks = models.CharField(max_length=250, null=True, blank=True, choices=remarks)
	Status = models.CharField(max_length=20, null=True, blank=True, choices=status)
	leasing_remark = models.CharField(max_length=225, null=True, blank=True)
	history = HistoricalRecords()

	def __str__(self):
		return self.PLATE_NO
				
	def get_absolute_url(self):
		return reverse('vehicle-list')


def increment_Activity_Id():
		last_in = Leasing.objects.all().order_by('id').last()
		if not last_in:
			return 'L' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
		in_id = last_in.Activity_Id
		in_int = int(in_id[8:])
		new_in_int = in_int + 1
		new_in_id = 'L' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
		return new_in_id


class Leasing(models.Model):

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
            )

	Activity_Id  = models.CharField(max_length=100,null=True, default=increment_Activity_Id)
	PLATE_NUMBER = models.CharField(max_length=100, null=True, blank=True)
	CS_NO= models.CharField(max_length=100, null=True, blank=True)
	COMPANY= models.CharField(max_length=100, null=True, blank=True)
	MODEL = models.CharField(max_length=100, null=True, blank=True)
	BRAND= models.CharField(max_length=100, null=True, blank=True, choices=Vbrand)
	VEHICLE_MAKE= models.CharField(max_length=100, null=True, blank=True)
	VEHICLE_TYPE= models.CharField(max_length=100, null=True, blank=True)
	LAST_NAME_ASSIGNEE= models.CharField(max_length=100, null=True, blank=True)
	FIRST_NAME_ASSIGNEE= models.CharField(max_length=100, null=True, blank=True)
	VEHICLE_CATEGORY= models.CharField(max_length=100, null=True, blank=True)
	COST_CENTER= models.CharField(max_length=100, null=True, blank=True)
	ID_NUMBER= models.CharField(max_length=100, null=True, blank=True)
	BAND= models.CharField(max_length=100, null=True, blank=True)
	GROUP= models.CharField(max_length=100, null=True, blank=True)
	DIVISION= models.CharField(max_length=100, null=True, blank=True)
	DEPARTMENT= models.CharField(max_length=100, null=True, blank=True)
	SECTION= models.CharField(max_length=100, null=True, blank=True)
	IS_EMPLOYEE_ID= models.CharField(max_length=100, null=True, blank=True)
	IS_LASTNAME= models.CharField(max_length=100, null=True, blank=True)
	IS_FIRSTNAME= models.CharField(max_length=100, null=True, blank=True)
	LOCATION= models.CharField(max_length=100, null=True, blank=True)
	AREA= models.CharField(max_length=100, null=True, blank=True)
	ACQUISITION_DATE= models.CharField(max_length=100, null=True, blank=True)
	remarks= models.CharField(max_length=250, null=True, blank=True)
	acquisition_cost= models.CharField(max_length=100, null=True, blank=True)
	months_36= models.CharField(max_length=100, null=True, blank=True)
	amount1= models.CharField(max_length=100, null=True, blank=True)
	date_in_1= models.CharField(max_length=100, null=True, blank=True)
	date_out_1= models.CharField(max_length=100, null=True, blank=True)
	months_24= models.CharField(max_length=100, null=True, blank=True)
	amount_Vat_EX= models.CharField(max_length=100, null=True, blank=True)
	date_in_2= models.CharField(max_length=100, null=True, blank=True)
	date_out_2= models.CharField(max_length=100, null=True, blank=True)
	extension= models.CharField(max_length=100, null=True, blank=True)
	amount2= models.CharField(max_length=100, null=True, blank=True)
	date_in_3= models.CharField(max_length=100, null=True, blank=True)
	date_out_3= models.CharField(max_length=100, null=True, blank=True)
	chasis_no= models.CharField(max_length=100, null=True, blank=True)
	engine_no= models.CharField(max_length=100, null=True, blank=True)
	CONTRACT_NUMBER= models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return self.Activity_Id
				
	def get_absolute_url(self):
		return reverse('leasing_list')




