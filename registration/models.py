from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date
from dateutil import tz

# History
from simple_history.models import HistoricalRecords


def increment_Activity_Id():
	last_in = Registration.objects.all().order_by('id').last()
	if not last_in:
	    return 'REG' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_Id
	in_int = int(in_id[8:])
	new_in_int = in_int + 1
	new_in_id = 'REG' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

def increment_NO():
	last_in = Registration.objects.all().order_by('id').last()
	if not last_in:
	    return '000001'
	in_id = last_in.NO
	in_int = int(in_id[0:])
	new_in_int = in_int + 1
	new_in_id = str(new_in_int).zfill(6)
	return new_in_id


class Registration(models.Model):
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
            ('Without Last Registration Date','Without Last Registration Date'),
            ('Without Smoke Emission Date','Without Smoke Emission Date'),
            ('Without COC Date','Without COC Date'),
            ('No Smoke and COC', 'No Smoke and COC'),
            ('For Registration', 'For Registration'),
            ('Complete','Complete'),
            )

	status = (
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
	MODEL = models.CharField(max_length=10, null=True, blank=True)
	BRAND = models.CharField(max_length=100, null=True, choices=Vbrand)
	VEHICLE_MAKE = models.CharField(max_length=100, null=True, blank=True)
	ENGINE_NO = models.CharField(max_length=100, null=True, blank=True)
	CHASSIS_NO = models.CharField(max_length=100, null=True, blank=True)
	MV_FILE_NO = models.CharField(max_length=100, null=True, blank=True)
	COC = models.CharField(max_length=225, null=True, blank=True)
	SMOKE_TPL = models.CharField(max_length=225, null=True, blank=True)
	REMARKS_REGISTERED = models.CharField(max_length=225, null=True, blank=True)
	DATE_EMAILED = models.CharField(max_length=225, null=True, blank=True)
	JUSTIFICATION_REMARKS = models.CharField(max_length=225, null=True, blank=True)
	Registration_month = models.CharField(max_length=10, null=True, blank=True)
	sent_email = models.CharField(max_length=10, null=True, blank=True,choices=status)
	history = HistoricalRecords()

	def __str__(self):
		return self.PLATE_NO
				
	def get_absolute_url(self):
		return reverse('Registration/January')


#### Email test table ####
class CarRegistration(models.Model):
    car = models.CharField(max_length=30)
    month = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    sent_email = models.CharField(max_length=10)
    def __str__(self):
    	return self.car
				

		