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
			'products_restriction': forms.Select(attrs={'class':'form-control', 'choices':'restrictions'}),
			'req_employee': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
			'req_fname': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
			'req_lname': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
			'req_title': forms.TextInput(attrs={'class':'form-control'}),
			'req_cost_center': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
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
			'SVV_SLA': forms.TextInput(attrs={'class':'form-control','value':'60','hidden':'true'})
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

	class Meta:
		model = Vehicle_Repair
		fields = [
		'request_date','employee','cost_center','first_name','last_name','contact_no','company','department','group_section',
		'plate_no','v_brand','engine','v_make','v_model','chassis','band','cond_sticker','equipment_no','fleet_area',
		'maintenance_type1','scope_work1','maintenance_type2','scope_work2','recommendations','service_reminder','verified_by', 
		'particulars','category','work_order1','work_order2','work_order3','datework_created','Shop_vendor','date_forwarded','estimate_no',
		'maintenance_amount','less_discount','estimate_remarks','estimate_attached','approvedby','meter_reading','VRR_SLA','memo_app'
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

		widgets ={
			'request_date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'employee' : forms.Select(attrs={'class':'form-control', 'readonly':'true'}),
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
			'VRR_SLA': forms.TextInput(attrs={'class':'form-control','value':'30','hidden':'true'})
		}