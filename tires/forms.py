from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import tire

class tireform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(tireform, self).__init__(*args, **kwargs)
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
		model = tire
		fields = [
		'request_date','employee','cost_center','first_name','last_name','contact_no','company','department','group_section',
		'plate_no','v_brand','engine','v_make','v_model','chassis','band','cond_sticker','equipment_no','fleet_area',
		'maintenance_type1','scope_work1','maintenance_type2','scope_work2','recommendations','service_reminder','verified_by', 
		'particulars','category','work_order1','work_order2','work_order3','datework_created','Shop_vendor','date_forwarded','estimate_no',
		'maintenance_amount','less_discount','estimate_remarks','estimate_attached','approvedby','meter_reading','VRR_SLA','memo_app','email'
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
			'email':forms.TextInput(attrs={'class':'form-control', 'type':'email'})
		}