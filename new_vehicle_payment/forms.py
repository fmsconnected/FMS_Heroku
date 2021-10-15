from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import (
	VehiclePayment
	)


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
		self.fields['Status'].required = True

		
	class Meta:

		model = VehiclePayment
		fields = ['A_employee_ID', 'E_First_name', 'E_Last_name', 'V_deliverDate','Plate_no',
		            'V_model','V_brand','V_make','V_dealer','LTO_documents',
		            'Docs_plate_no','LTO_stickers','Sticker_fields','Date_initial', 'First_payment', 'LTO_charges',
		            'Outstanding_balance','Date_final','Routing_remarks','V_SLA','rfp_number','invoice_number','equip_no','asset_no',
		            'sap_no','mat_no','Dealer_name','Status']
		status = (
			('Ongoing', 'Ongoing'),
			('Completed', 'Completed'),
		)

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
		    'V_SLA': forms.TextInput(attrs={'class':'form-control','type':'number','value':'30','hidden':'True'}),
		    'rfp_number' : forms.TextInput(attrs={'class':'form-control'}),
		    'invoice_number' : forms.TextInput(attrs={'class':'form-control'}),
		    'equip_no' : forms.TextInput(attrs={'class': 'form-control', 'readonly':'true'}),
		    'asset_no' : forms.TextInput(attrs={'class': 'form-control', 'readonly':'true'}),
		    'sap_no' : forms.TextInput(attrs={'class': 'form-control', 'readonly':'true'}),
		    'mat_no' : forms.TextInput(attrs={'class': 'form-control', 'readonly':'true'}),
		    'Dealer_name' : forms.TextInput(attrs={'class': 'form-control', 'readonly':'true'}),
		    'Status': forms.Select(attrs={'class':'form-control','choices':'status', 'required':'true'}),
		}
