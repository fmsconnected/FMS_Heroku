from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import CarRentalRequest, Gas_card, service_vehicle, Vehicle_Repair



class carrequestform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(carrequestform, self).__init__(*args, **kwargs)
		self.fields['Time'].required = False
		self.fields['Assignee_ATD'].required = False
		self.fields['Assignee_Section'].required = False
		self.fields['Assignee_band'].required = False
		self.fields['Type_of_vehicle'].required = False
		self.fields['Plate_no'].required = False
		self.fields['Immediate_supervisor'].required = False
		self.fields['Up_to'].required = False

	class Meta:
		model = CarRentalRequest
		fields = [
				'A_Employee','Date_received','Assignee_Fname','Assignee_Lname','Assignee_No',
				'Assignee_Company','Assignee_band','Assignee_Dept','Assignee_Cost','Assignee_Div','Assignee_Loc',
				'Assignee_Section','Assignee_Designation','Assignee_ATD','Vendor_name','Date','Up_to','Time',
				'Place_of_del','type_rental','Cost_center','Rental_period','Destination','Delivery_date',
				'End_user','Type_of_vehicle','Plate_no','Immediate_supervisor','CR_SLA'
		]
		CHOICES= (
			('Ser Roy DelaCruz', 'Ser Roy DelaCruz'),
			('Adolfo Carlos Umali', 'Adolfo Carlos Umali'),
			)
		Rental= (
			('Daily', 'Daily'),
			('Monthly', 'Monthly'),
			)
		Vtype= (
				('Sedan', 'Sedan'),
				('SUV', 'SUV'),
				('VAN', 'VAN'),
			)
		widgets = {
			'A_Employee' : forms.TextInput(attrs={'class':'form-control'}),
			'Date_received': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
			'Assignee_Fname': forms.TextInput(attrs={'class':'form-control'}),
			'Assignee_Lname': forms.TextInput(attrs={'class':'form-control'}),
			'Assignee_No': forms.TextInput(attrs={'class':'form-control','type':'tel'}),
			'Assignee_Company': forms.TextInput(attrs={'class':'form-control'}),
			'Assignee_band': forms.TextInput(attrs={'class':'form-control'}),
			'Assignee_Dept': forms.TextInput(attrs={'class':'form-control'}),
			'Assignee_Cost': forms.TextInput(attrs={'class':'form-control'}),
			'Assignee_Div' : forms.TextInput(attrs={'class':'form-control'}),
			'Assignee_Loc': forms.TextInput(attrs={'class':'form-control'}),
			'Assignee_Section': forms.TextInput(attrs={'class':'form-control'}),
			'Assignee_Designation': forms.TextInput(attrs={'class':'form-control'}),
			'Assignee_ATD': forms.TextInput(attrs={'class':'form-control'}),
			'Vendor_name': forms.TextInput(attrs={'class':'form-control'}),
			'Date' : forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
			'Up_to': forms.TextInput(attrs={'class':'form-control'}),
			'Time' : forms.TextInput(attrs={'class':'form-control', 'type':'time'}),
			'Place_of_del': forms.TextInput(attrs={'class':'form-control'}),
			'type_rental': forms.Select(attrs={'class':'form-control','choices':'Rental'}),
			'Cost_center': forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
			'Rental_period' : forms.TextInput(attrs={'class':'form-control'}),
			'Destination' : forms.TextInput(attrs={'class':'form-control'}),
			'Delivery_date': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
			'End_user': forms.TextInput(attrs={'class':'form-control'}),
			'Type_of_vehicle': forms.Select(attrs={'class':'form-control', 'choices':'Vtype'}),
			'Plate_no': forms.TextInput(attrs={'class':'form-control'}),
			'Immediate_supervisor': forms.Select(attrs={'class':'form-control','choices':'CHOICES'}),
			'CR_SLA' : forms.TextInput(attrs={'class':'form-control','value':'2','hidden':'true'})
		}
