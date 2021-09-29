from django.db import models
import datetime
from django.utils import timezone
import datetime
from django.db.models import DateTimeField,DateField
from datetime import date,timedelta
from django.urls import reverse




class Petron_report(models.Model):

	RecordNumber= models.CharField(max_length=254, null=True, blank=True)
	StatementNo= models.CharField(max_length=254, null=True, blank=True)
	Account_Number= models.CharField(max_length=254, null=True, blank=True)
	StatementDate= models.DateField(auto_now=False, null=True, blank=True)
	PaymentDueDate= models.DateField(auto_now=False, null=True, blank=True)
	PeriodCovered= models.CharField(max_length=254, null=True, blank=True)
	CardNumber= models.CharField(max_length=254, null=True, blank=True)
	ChargingDepartment= models.CharField(max_length=254, null=True, blank=True)
	EmbossedName= models.CharField(max_length=254, null=True, blank=True)
	PlateNumber= models.CharField(max_length=254, null=True, blank=True)
	VehicleDescription= models.CharField(max_length=254, null=True, blank=True)
	InvoiceDate= models.DateTimeField(auto_now=False, null=True, blank=True)
	StationName= models.CharField(max_length=254, null=True, blank=True)
	StationAddress= models.CharField(max_length=254, null=True, blank=True)
	InvoiceNumber= models.CharField(max_length=254, null=True, blank=True)
	ProductName= models.CharField(max_length=254, null=True, blank=True)
	ProductQuantity= models.FloatField(max_length=254, null=True, blank=True)
	ProductAmount= models.FloatField(max_length=254, null=True, blank=True)
	DiscountPerLitre= models.FloatField(max_length=254, null=True, blank=True)
	DiscountAmount= models.FloatField(max_length=254, null=True, blank=True)
	NetAmount= models.FloatField(max_length=254, null=True, blank=True)
	Odometer= models.CharField(max_length=254, null=True, blank=True)
	KMDriven= models.CharField(max_length=254, null=True, blank=True)
	Php_Km= models.CharField(max_length=254, null=True, blank=True)
	Km_Li= models.CharField(max_length=254, null=True, blank=True)
	FuelLimit= models.CharField(max_length=254, null=True, blank=True)
	FuelLimitUnit= models.CharField(max_length=254, null=True, blank=True)
	Supplier = models.CharField(max_length=254, null=True, blank=True)
	Lubes_imit= models.CharField(max_length=254, null=True, blank=True)
	Lubes_limit_unit= models.CharField(max_length=254, null=True, blank=True)
	Services_limit= models.CharField(max_length=254, null=True, blank=True)
	Treats_limit= models.CharField(max_length=254, null=True, blank=True)
	Others_limits= models.CharField(max_length=254, null=True, blank=True)

	def __str__(self):
		return self.RecordNumber

	def get_absolute_url(self):
		return reverse('jan_monthly_report')

class Petron_pivot(models.Model):
	ChargingDepartment = models.CharField(max_length=254, null=True, blank=True)
	sum_product_amount = models.CharField(max_length=254, null=True, blank=True)
	sum_disc_amount = models.CharField(max_length=254, null=True, blank=True)
	sum_net_amount = models.CharField(max_length=254, null=True, blank=True)
