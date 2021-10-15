from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import (
	Fuel_supplier
	)


class FuelsupplierForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(FuelsupplierForm, self).__init__(*args, **kwargs)
		self.fields['Fuel_provider'].required = False
		self.fields['SOA_current_amount'].required = False
		self.fields['SOA_outstanding_amount'].required = False
		self.fields['Payee'].required = False
		self.fields['SOA_attached'].required = False
		self.fields['Date_forwarded'].required = False
		self.fields['F_SLA'].required = False
		self.fields['status'].required = True

	class Meta:
		model = Fuel_supplier
		fields = [
		'SOA_Date_received','Fuel_provider','SOA_billdate','SOA_current_amount','SOA_outstanding_amount'
		,'Payee','SOA_attached','Date_forwarded','F_SLA','status'
		]

		CHOICES= (
			('GLOBE', 'GLOBE'),
			('INNOVE', 'INNOVE'),
			('BAYAN', 'BAYAN'),
		)
		fuelpro = (
			('SHELL','SHELL'),
			('Petron Corporation','Petron Corporation'),
			('Pilipinas Shell Petroleum Corp.','Pilipinas Shell Petroleum Corp.')
		)
		status=(
			('Ongoing','Ongoing'),
			('Completed','Completed'),
		)
		widgets = {

		'SOA_Date_received': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'Fuel_provider': forms.TextInput(attrs={'class':'form-control'}),
		'SOA_billdate': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'SOA_current_amount': forms.TextInput(attrs={'class':'form-control'}),
		'SOA_outstanding_amount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'Payee': forms.Select(attrs={'class':'form-control','choices':'CHOICES'}),
		'SOA_attached': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
		'Date_forwarded': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'F_SLA': forms.TextInput(attrs={'class':'form-control','type':'number','value':'15','hidden':'True'}),
		'status': forms.Select(attrs={'class':'form-control','choices':'status'}),
		}

		

