from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import (
	Vehicle_Repair_payment
	)

class vrepair_form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(vrepair_form, self).__init__(*args, **kwargs)
		self.fields['dealership'].required = False
		self.fields['amount'].required = False
		self.fields['service_type'].required = False
		self.fields['rfp_no'].required = False
		self.fields['invoice_number2'].requred = False
		self.fields['invoice_date'].required = False
		self.fields['Status'].required = True
	class Meta:
		model = Vehicle_Repair_payment
		fields = ['request_date','employee','cost_center','first_name','last_name','contact_no','company',
		'department','group_section','plate_no','v_brand','engine','v_make','v_model','chassis','band',
		'cond_sticker','equipment_no','dealership','amount','service_type','rfp_no','invoice_number2','invoice_date','Status'
		]
		maintenance= (
			('Preventive Maintenance','Preventive Maintenance'),
			('Corective Maitenance','Corective Maitenance'),
			('Battery','Battery'),
			('Tire','Tire'),
		)
		status = (
			('Ongoing', 'Ongoing'),
			('Completed', 'Completed'),
		)
		widgets	={

		'request_date': forms.TextInput(attrs={'class':'form-control', 'type':'date', 'readonly':'true'}), 
		'employee' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'cost_center' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'first_name' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'last_name' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'contact_no' : forms.TextInput(attrs={'class':'form-control'}),
		'company' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'department' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'group_section' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'plate_no' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'v_brand' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'engine' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'v_make' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'v_model' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'chassis' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'band' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'cond_sticker' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'equipment_no' : forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
		'dealership' : forms.TextInput(attrs={'class':'form-control'}),
		'amount' : forms.TextInput(attrs={'class':'form-control'}),
		'service_type': forms.Select(attrs={'class':'form-control','choices':'maintenance'}),
		'rfp_no': forms.TextInput(attrs={'class':'form-control'}),
		'invoice_number2': forms.TextInput(attrs={'class':'form-control'}),
		'invoice_date': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
		'Status': forms.Select(attrs={'class':'form-control', 'choices':'status'}),
	}

		

