from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import (
      Leasing
      )

class leasing_form(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super(leasing_form, self).__init__(*args, **kwargs)
            self.fields['CS_NO'].required = False
            self.fields['MODEL'].required = False
            self.fields['PLATE_NUMBER'].required = False
            self.fields['acquisition_cost'].required = False
            self.fields['amount1'].required = False
            self.fields['date_in_1'].required = False
            self.fields['date_out_1'].required = False
            self.fields['amount_Vat_EX'].required = False
            self.fields['date_in_2'].required = False
            self.fields['date_out_2'].required = False
            self.fields['extension'].required = False
            self.fields['amount2'].required = False
            self.fields['date_in_3'].required = False
            self.fields['date_out_3'].required = False
            self.fields['chasis_no'].required = False
            self.fields['months_36'].required = False
            self.fields['months_24'].required = False
            self.fields['engine_no'].required = False
            
      class Meta:
            model = Leasing
            fields = [
                  'PLATE_NUMBER', 'CS_NO', 'COMPANY', 'MODEL', 'BRAND', 'VEHICLE_MAKE', 'VEHICLE_TYPE', 'LAST_NAME_ASSIGNEE',
                  'FIRST_NAME_ASSIGNEE', 'VEHICLE_CATEGORY', 'COST_CENTER', 'ID_NUMBER', 'BAND', 'GROUP', 'DIVISION', 
                  'DEPARTMENT', 'SECTION', 'IS_EMPLOYEE_ID', 'IS_LASTNAME', 'IS_FIRSTNAME', 'LOCATION', 'AREA', 
                  'ACQUISITION_DATE', 'remarks', 'acquisition_cost', 'months_36', 'amount1', 'date_in_1', 'date_out_1', 
                  'months_24', 'amount_Vat_EX', 'date_in_2', 'date_out_2', 'extension', 'amount2', 'date_in_3', 'date_out_3', 
                  'chasis_no', 'engine_no', 'CONTRACT_NUMBER'
            ]

            Vbrand= (
                  ('Honda','Honda'),
                  ('Toyota','Toyota'),
                  ('Mitsubishi','Mitsubishi'),
                  ('Ford','Ford'),
                  ('Masda','Masda'),
                  ('Isuzu','Isuzu'),
                  ('Hyundai','Hyundai'),
                  ('Nissan','Nissan'),
                  ('SuZuki','Suzuki'),
                  ('Chevrolet','Chevrolet'),
                  ('Audi','Audi'),
                  ('BMW','BMW'),
                  ('Bently','Bently'),
                  ('Cadillac','Cadillac'),
                  ('Chrysler','Chrysler'),
                  ('Dodge','Dodge'),
                  ('GMC','GMC'),
                  ('Genesis','Genesis'),
                  ('Jaguar','Jaguar'),
                  ('Land Rover','Land Rover'),
                  ('Lexus','Lexus'),
                  ('Lincoln','Lincoln'),
                  ('Lotus','Lotus'),
                  ('Maserati','Maserati'),
                  ('Mercedes-Benz','Mercedes-Benz'),
                  ('Mini','Mini'),
                  ('Porsche','Porsche'),
                  ('Ram','Ram'),
                  ('Rolls-Royce','Rolls-Royce'),
                  ('Saab','Saab'),
                  ('Scion','Scion'),
                  ('Subaru','Subaru'),
                  ('Tesla','Tesla'),
                  ('Volkswagen','Volkswagen'),
                  ('Volvo','Volvo'),
                  ('Saturn','Saturn'),
            )

            widgets = {
      
                  'PLATE_NUMBER' : forms.TextInput(attrs={'class':'form-control'}),
                  'CS_NO' : forms.TextInput(attrs={'class':'form-control'}),
                  'COMPANY' : forms.TextInput(attrs={'class':'form-control'}),
                  'MODEL' : forms.TextInput(attrs={'class':'form-control'}),
                  'BRAND' : forms.Select(attrs={'class':'form-control','choices':'Vbrand'}),
                  'VEHICLE_MAKE' : forms.TextInput(attrs={'class':'form-control'}),
                  'VEHICLE_TYPE' : forms.TextInput(attrs={'class':'form-control'}),
                  'LAST_NAME_ASSIGNEE' : forms.TextInput(attrs={'class':'form-control'}),
                  'FIRST_NAME_ASSIGNEE' : forms.TextInput(attrs={'class':'form-control'}),
                  'VEHICLE_CATEGORY' : forms.TextInput(attrs={'class':'form-control'}),
                  'COST_CENTER' : forms.TextInput(attrs={'class':'form-control'}),
                  'ID_NUMBER' : forms.TextInput(attrs={'class':'form-control'}),
                  'BAND' : forms.TextInput(attrs={'class':'form-control'}),
                  'GROUP' : forms.TextInput(attrs={'class':'form-control'}),
                  'DIVISION' : forms.TextInput(attrs={'class':'form-control'}),
                  'DEPARTMENT' : forms.TextInput(attrs={'class':'form-control'}),
                  'SECTION' : forms.TextInput(attrs={'class':'form-control'}),
                  'IS_EMPLOYEE_ID' : forms.TextInput(attrs={'class':'form-control'}),
                  'IS_LASTNAME' : forms.TextInput(attrs={'class':'form-control'}),
                  'IS_FIRSTNAME' : forms.TextInput(attrs={'class':'form-control'}),
                  'LOCATION' : forms.TextInput(attrs={'class':'form-control'}),
                  'AREA' : forms.TextInput(attrs={'class':'form-control'}),
                  'ACQUISITION_DATE' : forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
                  'remarks' : forms.Textarea(attrs={'class':'form-control', 'rows':3, 'cols':40}),
                  'acquisition_cost' : forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
                  'months_36' : forms.TextInput(attrs={'class':'form-control'}),
                  'amount1' : forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
                  'date_in_1' : forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
                  'date_out_1' : forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
                  'months_24' : forms.TextInput(attrs={'class':'form-control'}),
                  'amount_Vat_EX' : forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
                  'date_in_2' : forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
                  'date_out_2' : forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
                  'extension' : forms.TextInput(attrs={'class':'form-control'}),
                  'amount2' : forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
                  'date_in_3' : forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
                  'date_out_3' : forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
                  'chasis_no' : forms.TextInput(attrs={'class':'form-control'}),
                  'engine_no' : forms.TextInput(attrs={'class':'form-control'}),
                  'CONTRACT_NUMBER' : forms.TextInput(attrs={'class':'form-control'}),
            }

