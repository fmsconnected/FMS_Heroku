from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import (
	Petron_report
	)


class petron_form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(petron_form, self).__init__(*args, **kwargs)
		self.fields['RecordNumber'].required = True
		self.fields['StatementNo'].required = True
		self.fields['Account_Number'].required = True
		self.fields['StatementDate'].required = True
		self.fields['PaymentDueDate'].required = False
		self.fields['PeriodCovered'].required = False
		self.fields['CardNumber'].required = False
		self.fields['ChargingDepartment'].required = True
		self.fields['EmbossedName'].required = False
		self.fields['PlateNumber'].required = False
		self.fields['VehicleDescription'].required = False
		self.fields['InvoiceDate'].required = True
		self.fields['StationName'].required = False
		self.fields['StationAddress'].required = False
		self.fields['InvoiceNumber'].required = False
		self.fields['ProductName'].required = False
		self.fields['ProductQuantity'].required = False
		self.fields['ProductAmount'].required = False
		self.fields['DiscountPerLitre'].required = False
		self.fields['DiscountAmount'].required = False
		self.fields['NetAmount'].required = False
		self.fields['Odometer'].required = False
		self.fields['KMDriven'].required = False
		self.fields['Php_Km'].required = False
		self.fields['Km_Li'].required = False
		self.fields['FuelLimit'].required = False
		self.fields['FuelLimitUnit'].required = False
		self.fields['Supplier'].required = False

	class Meta:
		model = Petron_report
		fields = ['RecordNumber','StatementNo','Account_Number','StatementDate','PaymentDueDate',
		'PeriodCovered','CardNumber','ChargingDepartment','EmbossedName','PlateNumber','VehicleDescription',
		'InvoiceDate','StationName','StationAddress','InvoiceNumber','ProductName','ProductQuantity',
		'ProductAmount','DiscountPerLitre','DiscountAmount','NetAmount','Odometer','KMDriven','Php_Km',
		'Km_Li','FuelLimit','FuelLimitUnit','Supplier']
		widgets = {
		'RecordNumber': forms.TextInput(attrs={'class':'form-control'}),
		'StatementNo': forms.TextInput(attrs={'class':'form-control'}),
		'Account_Number': forms.TextInput(attrs={'class':'form-control'}),
		'StatementDate': forms.TextInput(attrs={'class':'form-control'}),
		'PaymentDueDate': forms.TextInput(attrs={'class':'form-control','type':'Date'}),
		'PeriodCovered': forms.TextInput(attrs={'class':'form-control'}),
		'CardNumber': forms.TextInput(attrs={'class':'form-control'}),
		'ChargingDepartment': forms.TextInput(attrs={'class':'form-control'}),
		'EmbossedName': forms.TextInput(attrs={'class':'form-control'}),
		'PlateNumber': forms.TextInput(attrs={'class':'form-control'}),
		'VehicleDescription': forms.TextInput(attrs={'class':'form-control'}),
		'InvoiceDate': forms.TextInput(attrs={'class':'form-control','type':'Date'}),
		'StationName': forms.TextInput(attrs={'class':'form-control'}),
		'StationAddress': forms.TextInput(attrs={'class':'form-control'}),
		'InvoiceNumber': forms.TextInput(attrs={'class':'form-control','type':'Number'}),
		'ProductName': forms.TextInput(attrs={'class':'form-control'}),
		'ProductQuantity': forms.TextInput(attrs={'class':'form-control','type':'Number'}),
		'ProductAmount': forms.TextInput(attrs={'class':'form-control','type':'Number'}),
		'DiscountPerLitre': forms.TextInput(attrs={'class':'form-control','type':'Number'}),
		'DiscountAmount': forms.TextInput(attrs={'class':'form-control','type':'Number'}),
		'NetAmount': forms.TextInput(attrs={'class':'form-control','type':'Number'}),
		'Odometer': forms.TextInput(attrs={'class':'form-control'}),
		'KMDriven': forms.TextInput(attrs={'class':'form-control'}),
		'Php_Km': forms.TextInput(attrs={'class':'form-control'}),
		'Km_Li': forms.TextInput(attrs={'class':'form-control'}),
		'FuelLimit': forms.TextInput(attrs={'class':'form-control','type':'Number'}),
		'FuelLimitUnit': forms.TextInput(attrs={'class':'form-control','type':'Number'}),
		'Supplier': forms.TextInput(attrs={'class':'form-control', 'value':'Petron','hidden':'true'})
		}