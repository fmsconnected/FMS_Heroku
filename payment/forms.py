from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import VehiclePayment,Fuel_supplier, Vehicle_Repair_payment


class VehiclePaymentform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(VehiclePaymentform, self).__init__(*args, **kwargs)
		self.fields['LTO_documents'].required = False
		self.fields['Docs_plate_no'].required = False
		self.fields['LTO_stickers'].required = False
		self.fields['Sticker_fields'].required = False
		self.fields['Date_initial'].required = False
		self.fields['First_payment'].required = False
		self.fields['LTO_charges'].required = False
		self.fields['Outstanding_balance'].required = False
		self.fields['Date_final'].required = False
		self.fields['Routing_remarks'].required = False
		self.fields['rfp_number'].required = False
		self.fields['invoice_number'].required = False
		self.fields['equip_no'].required = False
		self.fields['asset_no'].required = False
		self.fields['sap_no'].required = False
		self.fields['mat_no'].required = False
		self.fields['Dealer_name'].required = False

		
	class Meta:
		model = VehiclePayment
		fields = ['A_employee_ID', 'E_First_name', 'E_Last_name', 'V_deliverDate','Plate_no',
		            'V_model','V_brand','V_make','V_dealer','LTO_documents',
		            'Docs_plate_no','LTO_stickers','Sticker_fields','Date_initial', 'First_payment', 'LTO_charges',
		            'Outstanding_balance','Date_final','Routing_remarks','V_SLA','rfp_number','invoice_number','equip_no','asset_no',
		            'sap_no','mat_no','Dealer_name']
		widgets = {
			'A_employee_ID': forms.TextInput(attrs={'class':'form-control'}),
			'E_First_name': forms.TextInput(attrs={'class':'form-control'}),
			'E_Last_name': forms.TextInput(attrs={'class':'form-control'}),
			'V_deliverDate': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'Plate_no': forms.TextInput(attrs={'class':'form-control'}),
		    'V_model': forms.TextInput(attrs={'class':'form-control'}),
		    'V_brand': forms.TextInput(attrs={'class':'form-control'}),
		    'V_make': forms.TextInput(attrs={'class':'form-control'}),
		    'V_dealer': forms.TextInput(attrs={'class':'form-control'}),
		    'LTO_documents': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		    'Docs_plate_no': forms.TextInput(attrs={'class':'form-control'}),
		    'LTO_stickers': forms.TextInput(attrs={'class':'form-control'}),
		    'Sticker_fields': forms.TextInput(attrs={'class':'form-control'}),
		    'Date_initial': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
		    'First_payment': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		    'LTO_charges': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		    'Outstanding_balance': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		    'Date_final': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		    'Routing_remarks': forms.TextInput(attrs={'class':'form-control'}),
		    'V_SLA': forms.TextInput(attrs={'class':'form-control','type':'number','value':'15','hidden':'True'}),
		    'rfp_number' : forms.TextInput(attrs={'class':'form-control'}),
		    'invoice_number' : forms.TextInput(attrs={'class':'form-control'}),
		    'equip_no' : forms.TextInput(attrs={'class': 'form-control', 'readonly':'true'}),
		    'asset_no' : forms.TextInput(attrs={'class': 'form-control', 'readonly':'true'}),
		    'sap_no' : forms.TextInput(attrs={'class': 'form-control', 'readonly':'true'}),
		    'mat_no' : forms.TextInput(attrs={'class': 'form-control', 'readonly':'true'}),
		    'Dealer_name' : forms.TextInput(attrs={'class': 'form-control', 'readonly':'true'})
		}

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

	class Meta:
		model = Fuel_supplier
		fields = [
		'SOA_Date_received','Fuel_provider','SOA_billdate','SOA_current_amount','SOA_outstanding_amount'
		,'Payee','SOA_attached','Date_forwarded','F_SLA'
		]

		CHOICES= (
			('GLOBE', 'GLOBE'),
			('INNOVE', 'INNOVE'),
			('BAYAN', 'BAYAN'),
		)
		widgets = {

		'SOA_Date_received': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'Fuel_provider': forms.TextInput(attrs={'class':'form-control'}),
		'SOA_billdate': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'SOA_current_amount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'SOA_outstanding_amount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'Payee': forms.Select(attrs={'class':'form-control','choices':'CHOICES'}),
		'SOA_attached': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
		'Date_forwarded': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'F_SLA': forms.TextInput(attrs={'class':'form-control','type':'number','value':'15','hidden':'True'})
		}

class vrepair_form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(vrepair_form, self).__init__(*args, **kwargs)
		self.fields['dealership'].required = False
		self.fields['amount'].required = False
		self.fields['service_type'].required = False
		self.fields['rfp_no'].required = False
		self.fields['invoice_number2'].requred = False
		self.fields['invoice_date'].required = False
	class Meta:
		model = Vehicle_Repair_payment
		fields = ['request_date','employee','cost_center','first_name','last_name','contact_no','company',
		'department','group_section','plate_no','v_brand','engine','v_make','v_model','chassis','band',
		'cond_sticker','equipment_no','dealership','amount','service_type','rfp_no','invoice_number2','invoice_date'
		]
		maintenance= (
		('Preventive Maintenance','Preventive Maintenance'),
		('Corective Maitenance','Corective Maitenance'),
		('Battery','Battery'),
		('Tire','Tire'),
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
	}



