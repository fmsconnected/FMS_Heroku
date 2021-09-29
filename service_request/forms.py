from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import service_vehicle




class serviceform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(serviceform, self).__init__(*args, **kwargs)
		self.fields['req_employee_id'].required = False
		self.fields['assignee_employee_id'].required = False
		self.fields['assignee_group'].required = False
		self.fields['assignee_fname'].required = False
		self.fields['assignee_lname'].required = False
		self.fields['assignee_costcenter'].required = False
		self.fields['assignee_section'].required = False
		self.fields['assignee_location'].required = False
		self.fields['assignee_atd'].required = False
		self.fields['new_employee_id'].required = False
		self.fields['new_employee_fname'].required = False
		self.fields['new_employee_lname'].required = False
		self.fields['new_employee_cost'].required = False
		self.fields['new_temporary_atd'].required = False
		self.fields['prefered_vehicle'].required = False
		self.fields['justification'].required = False
		self.fields['E_con_sticker'].required = False
		self.fields['E_model_year'].required = False
		self.fields['E_brand'].required = False
		self.fields['E_type'].required = False
		self.fields['approved_by'].required = False
		self.fields['approved_date'].required = False
		self.fields['vehicle_provider'].required = False
		self.fields['vehicle_plate_no'].required = False
		self.fields['vehicle_CS_no'].required = False
		self.fields['vehicle_model'].required = False
		self.fields['vehicle_brand'].required = False
		self.fields['vehicle_make'].required = False
		self.fields['vehicle_fuel_type'].required = False
		self.fields['SVV_SLA'].required = False

	class Meta:
		model = service_vehicle
		fields = [
			'request_date','req_employee_id','req_lname','req_fname','assignee_employee_id','assignee_group',
			'assignee_fname','assignee_lname','assignee_costcenter','assignee_section','assignee_location', 
			'assignee_atd','new_employee_id','new_employee_fname','new_employee_lname','new_employee_cost',
			'new_temporary_atd','prefered_vehicle','justification','E_plate_no','E_con_sticker','E_model_year','E_brand',
			'E_make','E_type','approved_by','approved_date','vehicle_provider','vehicle_plate_no','vehicle_CS_no',
			'vehicle_model','vehicle_brand','vehicle_make','vehicle_fuel_type','SVV_SLA'
		]
		vtype= (
			('Sedan', 'Sedan'),
			('SUV', 'SUV '),
			('Pick up 4x2', 'Pick up 4x2'),
			('Pick Up 4x4', 'Pick Up 4x4'),
			('AUV', 'AUV'),
			('Others', 'Others '),
			)
		approvedby= (
			('Ser Roy Dela Cruz', 'Ser Roy Dela Cruz'),
			('Adolfo Carlos Umali', 'Adolfo Carlos Umali '),
			)
		vprovider= (
			('Orix', 'Orix'),
			('Diamond', 'Diamond '),
			('Safari', 'Safari'),
			)
		vbrand= (
			('BMW', 'BMW'),
			('Chevrolet', 'Chevrolet '),
			('chrysler', 'chrysler'),
			('Ford', 'Ford'),
			('Honda', 'Honda '),
			('Hyundai', 'Hyundai'),
			('Isuzu', 'Isuzu'),
			('Kia', 'Kia '),
			('Masda', 'Masda'),
			('Mitsubishi', 'Mitsubishi'),
			('Nissan', 'Nissan '),
			('Peugeot', 'Peugeot'),
			('Subaro', 'Subaro'),
			)

		widgets = {	
			'request_date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'req_employee_id': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'req_lname': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'req_fname': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'assignee_employee_id': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'assignee_group': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'assignee_fname': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'assignee_lname': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'assignee_costcenter': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'assignee_section': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'assignee_location': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'assignee_atd': forms.TextInput(attrs={'class':'form-control'}),
			'new_employee_id': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'new_employee_fname': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'new_employee_lname': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'new_employee_cost': forms.TextInput(attrs={'class':'form-control', 'readonly':'True'}),
			'new_temporary_atd': forms.TextInput(attrs={'class':'form-control'}),
			'prefered_vehicle': forms.Select(attrs={'class':'form-control', 'choices':'vtype'}),
			'justification': forms.TextInput(attrs={'class':'form-control'}),
			'E_plate_no': forms.TextInput(attrs={'class':'form-control'}),
			'E_con_sticker': forms.TextInput(attrs={'class':'form-control'}),
			'E_model_year': forms.TextInput(attrs={'class':'form-control'}),
			'E_brand': forms.TextInput(attrs={'class':'form-control'}),
			'E_make': forms.TextInput(attrs={'class':'form-control'}),
			'E_type': forms.TextInput(attrs={'class':'form-control'}),
			'approved_by': forms.Select(attrs={'class':'form-control','choices':'approvedby'}),
			'approved_date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'vehicle_provider': forms.TextInput(attrs={'class':'form-control','choices':'vprovider'}),
			'vehicle_plate_no': forms.TextInput(attrs={'class':'form-control'}),
			'vehicle_CS_no': forms.TextInput(attrs={'class':'form-control'}),
			'vehicle_model': forms.TextInput(attrs={'class':'form-control'}),
			'vehicle_brand': forms.Select(attrs={'class':'form-control','choices':'vbrand'}),
			'vehicle_make': forms.TextInput(attrs={'class':'form-control'}),
			'vehicle_fuel_type': forms.TextInput(attrs={'class':'form-control'}),
			'SVV_SLA': forms.TextInput(attrs={'class':'form-control','value':'90','hidden':'true'})
		}
