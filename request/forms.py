from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Vehicle_Repair,Gas_card


class gascardform(forms.ModelForm):
    
	def __init__(self, *args, **kwargs):
		super(gascardform, self).__init__(*args, **kwargs)
		self.fields['approved_by'].required = False
		self.fields['date_summitted'].required = False
		self.fields['fleet_received'].required = False
		self.fields['fleet_card_no'].required = False
		self.fields['fleet_date_release'].required = False
		self.fields['person_release'].required = False
		self.fields['fleet_provider'].required = False
		self.fields['atd_no'].required = False
		self.fields['temporary_atd'].required = False
		self.fields['new_emp_id'].required = False
		self.fields['new_emp_fname'].required = False
		self.fields['new_emp_lname'].required = False
		self.fields['new_emp_cost'].required = False
		self.fields['new_temp_atd'].required = False
		self.fields['new_assignee'].required = False
		self.fields['cost_center_code'].required = False
		self.fields['cancellation'].required = False
		self.fields['plate_no'].required = False
		self.fields['con_sticker'].required = False
		self.fields['model_year'].required = False
		self.fields['brand'].required = False
		self.fields['make'].required = False
		self.fields['fuel_type'].required = False
		self.fields['new_plate_no'].required = False
		self.fields['new_cond_sticker'].required = False
		self.fields['new_model_year'].required = False
		self.fields['new_vbrand'].required = False
		self.fields['new_vmake'].required = False
		self.fields['new_vfuel_type'].required = False
		self.fields['GCR_SLA'].required = False
	class Meta:
		model = Gas_card
		fields = [
				'date_received','application_type','fleet_provider','fleetcard_type',
				'fuel_limit_amount','fuel_limit_quantity','products_restriction','req_employee','req_fname','req_lname','req_title',
				'req_cost_center','atd_no','temporary_atd','new_emp_id','new_emp_fname','new_emp_lname','new_emp_cost',
				'new_temp_atd','new_assignee','cost_center_code','cancellation','plate_no','con_sticker','model_year','brand','make',
				'fuel_type','new_plate_no','new_cond_sticker','new_model_year','new_vbrand','new_vmake','new_vfuel_type',
				'approved_by','date_summitted','fleet_received','fleet_card_no','fleet_date_release','person_release','GCR_SLA'
		]
			
		card_type= (
			('Single', 'Single'),
			('Driver','Driver'),
			('Vehicle','Vehicle'),
			)
		fleet_card= (
			('Petron', 'Petron'),
			('Shell','Shell'),
		)
		app_type= (
			('Daily', 'Daily'),
			('Transfer Acountability', 'Transfer Acountability'),
			('Cancel - Disposal of Vehicle', 'Cancel - Disposal of Vehicle'),
			('Cancel - Resignation of User', 'Cancel - Resignation of User'),
			('Replacement - Damage', 'Replacement - Damage'),
			('Replacement - Lose', 'Replacement - Lose'),
			('Others - Adjust Credit Limit', 'Others - Adjust Credit Limit'),
			('Others - Change of Product Restriction', 'Others - Change of Product Restriction'),
			('Others - Update Cost Center', 'Others - Update Cost Center'),
			('Replacement - Expired card', 'Replacement - Expired card'),
		)
		restrictions= (
			('S: Super Only', 'S: Super Only'),
			('U: Super Unleaded Only', 'U: Super Unleaded Only'),
			('R: Regular Only', 'R: Regular Only'),
			('X: Velocity', 'X: Velocity'),
			('D: Diesoline Only', 'D: Diesoline Only'),
			('L: Lubricant Only', 'L: Lubricant Only'),
			('V: Service Only', 'V: Service Only'),
			('C: Convenience store items, sundries, accesories', 'C: Convenience store items, sundries, accesories'),
		)
		approved= (
			('Ser Roy Perluval Dela Cruz','Ser Roy Perluval Dela Cruz'),
		)
		cancellation= (
			('Disposal Of Vehicle','Disposal Of Vehicle'),
			('Resignation of User','Resignation of User'),
		)
		widgets = {
			'date_received': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'application_type': forms.Select(attrs={'class':'form-control', 'choices':'app_type'}),
			'fleet_provider': forms.Select(attrs={'class':'form-control', 'choices':'fleet_card'}),
			'fleetcard_type': forms.Select(attrs={'class':'form-control', 'choices':'card_type'}),
			'fuel_limit_amount': forms.TextInput(attrs={'class':'form-control'}),
			'fuel_limit_quantity': forms.TextInput(attrs={'class':'form-control'}),
			'products_restriction': forms.Select(attrs={'class':'form-control','choices':'restrictions'}),
			'req_employee': forms.TextInput(attrs={'class':'form-control'}),
			'req_fname': forms.TextInput(attrs={'class':'form-control'}),
			'req_lname': forms.TextInput(attrs={'class':'form-control'}),
			'req_title': forms.TextInput(attrs={'class':'form-control'}),
			'req_cost_center': forms.TextInput(attrs={'class':'form-control'}),
			'req_cost_center': forms.TextInput(attrs={'class':'form-control'}),
			'atd_no': forms.TextInput(attrs={'class':'form-control'}),
			'temporary_atd': forms.TextInput(attrs={'class':'form-control'}),
			'new_emp_id': forms.TextInput(attrs={'class':'form-control'}),
			'new_emp_fname': forms.TextInput(attrs={'class':'form-control'}),
			'new_emp_lname': forms.TextInput(attrs={'class':'form-control'}),
			'new_emp_cost': forms.TextInput(attrs={'class':'form-control'}),
			'new_temp_atd': forms.TextInput(attrs={'class':'form-control'}),
			'new_assignee': forms.TextInput(attrs={'class':'form-control'}),
			'cost_center_code': forms.TextInput(attrs={'class':'form-control'}),
			'cancellation': forms.Select(attrs={'class':'form-control', 'choices':'cancellation'}),
			'plate_no': forms.TextInput(attrs={'class':'form-control'}),
			'con_sticker': forms.TextInput(attrs={'class':'form-control'}),
			'model_year': forms.TextInput(attrs={'class':'form-control'}),
			'brand': forms.TextInput(attrs={'class':'form-control'}),
			'make': forms.TextInput(attrs={'class':'form-control'}),
			'fuel_type': forms.TextInput(attrs={'class':'form-control'}),
			'new_plate_no': forms.TextInput(attrs={'class':'form-control'}),
			'new_cond_sticker': forms.TextInput(attrs={'class':'form-control'}),
			'new_model_year': forms.TextInput(attrs={'class':'form-control','type':'number'}),
			'new_vbrand': forms.TextInput(attrs={'class':'form-control'}),
			'new_vmake': forms.TextInput(attrs={'class':'form-control'}),
			'new_vfuel_type': forms.TextInput(attrs={'class':'form-control'}),
			'approved_by' : forms.Select(attrs={'class':'form-control','choices':'approved'}),
			'date_summitted': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'fleet_received': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'fleet_card_no': forms.TextInput(attrs={'class':'form-control'}),
			'fleet_date_release' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'person_release' : forms.TextInput(attrs={'class':'form-control'}),
			'GCR_SLA': forms.TextInput(attrs={'class':'form-control','value':'10','hidden':'True'})
		}

class repairform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(repairform, self).__init__(*args, **kwargs)
		self.fields['contact_no'].required = False
		self.fields['particulars'].required = False
		self.fields['maintenance_type1'].required = False
		self.fields['scope_work1'].required = False
		self.fields['maintenance_type2'].required = False
		self.fields['scope_work2'].required = False
		self.fields['recommendations'].required = False
		self.fields['service_reminder'].required = False
		self.fields['verified_by'].required = False
		self.fields['work_order1'].required = False
		self.fields['work_order2'].required = False
		self.fields['work_order3'].required = False
		self.fields['datework_created'].required = False
		self.fields['Shop_vendor'].required = False
		self.fields['date_forwarded'].required = False
		self.fields['estimate_no'].required = False
		self.fields['maintenance_amount'].required = False
		self.fields['less_discount'].required = False
		self.fields['estimate_remarks'].required = False
		self.fields['estimate_attached'].required = False
		self.fields['approvedby'].required = False
		self.fields['meter_reading'].required = False
		self.fields['VRR_SLA'].required = False
		self.fields['memo_app'].required = False
		self.fields['status'].required = True

	class Meta:
		model = Vehicle_Repair
		fields = [
		'request_date','employee','cost_center','first_name','last_name','contact_no','company','department','group_section',
		'plate_no','v_brand','engine','v_make','v_model','chassis','band','cond_sticker','equipment_no','fleet_area',
		'maintenance_type1','scope_work1','maintenance_type2','scope_work2','recommendations','service_reminder','verified_by', 
		'particulars','category','work_order1','work_order2','work_order3','datework_created','Shop_vendor','date_forwarded','estimate_no',
		'maintenance_amount','less_discount','estimate_remarks','estimate_attached','approvedby','meter_reading','VRR_SLA','memo_app','email','status'
		]
		area= (
			('The Globe Tower', 'The Globe Tower'),
			('Visayas-Mindanao', 'Visayas-Mindanao '),
		)
		
		verified= (
			('Shane Santos','Shane Santos'),
		)
		# shop= (
		# 	('GR8','GR8'),
		# 	('Others','Others')
		# )
		maintenance= (
			('Preventive Maintenance','Preventive Maintenance'),
			('Corective Maitenance','Corective Maitenance'),
			('Battery','Battery'),
			('Tire','Tire'),
		)
		approvedby= (
			('Ser Roy Perluval Dela Cruz','Ser Roy Perluval Dela Cruz'),
			('Adolfo Carlos Umali','Adolfo Carlos Umali'),
		)
		vstatus = (
			('Ongoing', 'Ongoing'),
			('Completed', 'Completed'),
		)
		widgets ={
			'request_date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
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
			'fleet_area' : forms.Select(attrs={'class':'form-control','choices':'area'}),
			'particulars' : forms.TextInput(attrs={'class':'form-control'}),
			'category' : forms.TextInput(attrs={'class':'form-control'}),
			'maintenance_type1' : forms.Select(attrs={'class':'form-control','choices':'maintenance'}),
			'scope_work1' : forms.TextInput(attrs={'class':'form-control'}),
			'maintenance_type2' : forms.Select(attrs={'class':'form-control','choices':'maintenance'}),
			'scope_work2' : forms.TextInput(attrs={'class':'form-control'}),
			'recommendations' : forms.TextInput(attrs={'class':'form-control'}),
			'service_reminder' : forms.TextInput(attrs={'class':'form-control'}),
			'verified_by' : forms.Select(attrs={'class':'form-control','choices':'verified'}),
			'work_order1' : forms.TextInput(attrs={'class':'form-control'}),
			'work_order2' : forms.TextInput(attrs={'class':'form-control'}),
			'work_order3' : forms.TextInput(attrs={'class':'form-control'}),
			'datework_created': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'memo_app': forms.TextInput(attrs={'class':'form-control'}),
			'Shop_vendor' : forms.TextInput(attrs={'class':'form-control'}),
			'date_forwarded' : forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
			'estimate_no' : forms.TextInput(attrs={'class':'form-control'}),
			'maintenance_amount' : forms.TextInput(attrs={'class':'form-control'}),
			'less_discount' : forms.TextInput(attrs={'class':'form-control'}),
			'estimate_remarks' : forms.TextInput(attrs={'class':'form-control'}),
			'estimate_attached' : forms.TextInput(attrs={'class':'form-control'}),
			'approvedby' : forms.Select(attrs={'class':'form-control','choices':'approvedby'}),
			'meter_reading' : forms.TextInput(attrs={'class':'form-control'}),
			'VRR_SLA': forms.TextInput(attrs={'class':'form-control','value':'30','hidden':'true'}),
			'email':forms.TextInput(attrs={'class':'form-control', 'type':'email'}),
			'status' : forms.Select(attrs={'class':'form-control','choices':'vstatus'}),
		}