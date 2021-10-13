from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date
# History
from simple_history.models import HistoricalRecords

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
	vstatus = (
			('Sold', 'Sold'),
			('Transferred', 'Transferred'),
			('Active', 'Active'),
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
	ACQUISITION_DATE= models.DateField(auto_now=False, null=True, blank=True)
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
	vleasing_status = models.CharField(max_length=100, null=True, blank=True, choices=vstatus)
	email = models.CharField(max_length=200, null=True, blank=True)
	history = HistoricalRecords()
	
	def __str__(self):
		return self.Activity_Id
				
	def get_absolute_url(self):
		return reverse('leasing_list')


