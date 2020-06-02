from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import (
      EmployeeMasterlist,
      VehicleMasterList,
      Leasing
      )




class EmpMasterlistForm(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super(EmpMasterlistForm, self).__init__(*args, **kwargs)
            self.fields['Suffix'].required = False
            self.fields['Unit'].required = False
            self.fields['Sub_unit'].required = False
            
      class Meta:
            model = EmployeeMasterlist
            fields = [
                  'Company','Employee_Id','Last_name','First_name','Middle_name','Suffix','Band','Cost_center','DIV_code','Group','Division',
                  'Department','Section','Unit','Sub_unit','IS_ID','IS_lastname','IS_firstname','Location',
                  'Area','Area2','Benefit'
            ]
            widgets = {
                  'Company': forms.TextInput(attrs={'class':'form-control'}),
                  'Employee_Id':forms.TextInput(attrs={'class':'form-control'}),
                  'Last_name':forms.TextInput(attrs={'class':'form-control'}),
                  'First_name':forms.TextInput(attrs={'class':'form-control'}),
                  'Middle_name':forms.TextInput(attrs={'class':'form-control'}),
                  'Suffix':forms.TextInput(attrs={'class':'form-control'}),
                  'Band':forms.TextInput(attrs={'class':'form-control'}),
                  'Cost_center':forms.TextInput(attrs={'class':'form-control','type':'number'}),
                  'DIV_code':forms.TextInput(attrs={'class':'form-control'}),
                  'Group':forms.TextInput(attrs={'class':'form-control'}),
                  'Division':forms.TextInput(attrs={'class':'form-control'}),
                  'Department':forms.TextInput(attrs={'class':'form-control'}),
                  'Section':forms.TextInput(attrs={'class':'form-control'}),
                  'Unit':forms.TextInput(attrs={'class':'form-control'}),
                  'Sub_unit':forms.TextInput(attrs={'class':'form-control'}),
                  'IS_ID':forms.TextInput(attrs={'class':'form-control'}),
                  'IS_lastname':forms.TextInput(attrs={'class':'form-control'}),
                  'IS_firstname':forms.TextInput(attrs={'class':'form-control'}),
                  'Location':forms.TextInput(attrs={'class':'form-control'}),
                  'Area':forms.TextInput(attrs={'class':'form-control'}),
                  'Area2':forms.TextInput(attrs={'class':'form-control'}),
                  'Benefit':forms.TextInput(attrs={'class':'form-control'})
            }

class Vmasterlist(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super(Vmasterlist, self).__init__(*args, **kwargs)
            self.fields['PLATE_NO'].required = False
            self.fields['PLATE_ENDING'].required = False
            self.fields['REGISTRATION_MONTH'].required = False
            self.fields['BRAND'].required = False
            self.fields['VEHICLE_MAKE'].required = False
            self.fields['ENGINE_NO'].required = False
            self.fields['CHASSIS_NO'].required = False
            self.fields['MV_FILE_NO'].required = False
            self.fields['VEHICLE_TYPE'].required = False
            self.fields['ASSIGNEE_LAST_NAME'].required = False
            self.fields['ASSIGNEE_FIRST_NAME'].required = False
            self.fields['VEHICLE_CATEGORY'].required = False
            self.fields['Employee'].required = False
            self.fields['BAND_LEVEL'].required = False
            self.fields['BENEFIT_GROUP'].required = False
            self.fields['COST_CENTER'].required = False
            self.fields['GROUP'].required = False
            self.fields['DIVISION'].required = False
            self.fields['DEPARTMENT'].required = False
            self.fields['SECTION'].required = False
            self.fields['IS_ID'].required = False
            self.fields['IS_LAST_NAME'].required = False
            self.fields['IS_FIRST_NAME'].required = False
            self.fields['LOCATION'].required = False
            self.fields['ORIGINAL_OR_DATE'].required = False
            self.fields['ACQ_DATE'].required = False
            self.fields['ACQ_COST'].required = False
            self.fields['ASSET_NO'].required = False
            self.fields['EQUIPMENT_NO'].required = False
            self.fields['PO_NO'].required = False
            self.fields['SAP_PR'].required = False
            self.fields['Vehicle_IVN_no'].required = False
            self.fields['ASSET_NO'].required = False
            self.fields['Unit_MATDOC'].required = False
            self.fields['dealer'].required = False
            self.fields['dealer_name'].required = False
            self.fields['PLATE_NUMBER_RELEASE_DATE'].required = False
            self.fields['leasing_remark'].required = False

      class Meta:
            model = VehicleMasterList
            fields = [
                  'PLATE_NO','CS_NO','CR_NAME','PLATE_ENDING','REGISTRATION_MONTH','MODEL','BRAND',
                  'VEHICLE_MAKE','ENGINE_NO','CHASSIS_NO','MV_FILE_NO','VEHICLE_TYPE','ASSIGNEE_LAST_NAME','ASSIGNEE_FIRST_NAME','VEHICLE_CATEGORY','Employee',
                  'BAND_LEVEL','BENEFIT_GROUP','COST_CENTER','GROUP','DIVISION','DEPARTMENT','SECTION','IS_ID','IS_LAST_NAME','IS_FIRST_NAME','LOCATION','ORIGINAL_OR_DATE',
                  'ACQ_DATE','ACQ_COST','ASSET_NO','EQUIPMENT_NO', 'SAP_PR','Vehicle_IVN_no','Unit_MATDOC','dealer',
                  'dealer_name','PO_NO','PLATE_NUMBER_RELEASE_DATE','Last_Registration_Date','Smoke_Emission_Date', 'COC_Date', 'Remarks', 'Status', 'leasing_remark'
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
                  ('Jeep">Jeep'),
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
                  ('Kia','Kia'),
            )

            status = (
                  ('Yes', 'Yes'),
                  ('No', 'No'),
            )


            remarks = (
                  ('Without Last Registration Date','Without Last Registration Date'),
                  ('Without Smoke Emission Date','Without Smoke Emission Date'),
                  ('Without COC Date','Without COC Date'),
                  ('No Smoke and COC', 'No Smoke and COC'),
                  ('For Registration', 'For Registration'),
                  ('Complete','Complete'),
            )


            widgets = {
                  'PLATE_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'CS_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'CR_NAME': forms.TextInput(attrs={'class':'form-control'}),
                  'PLATE_ENDING': forms.TextInput(attrs={'class':'form-control', 'hidden':'true'}),
                  'REGISTRATION_MONTH': forms.TextInput(attrs={'class':'form-control'}),
                  'MODEL': forms.TextInput(attrs={'class':'form-control'}),
                  'BRAND': forms.Select(attrs={'class':'form-control','choices':'Vbrand'}),
                  'VEHICLE_MAKE': forms.TextInput(attrs={'class':'form-control'}),
                  'ENGINE_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'CHASSIS_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'MV_FILE_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'VEHICLE_TYPE': forms.TextInput(attrs={'class':'form-control'}),
                  'ASSIGNEE_LAST_NAME': forms.TextInput(attrs={'class':'form-control'}),
                  'ASSIGNEE_FIRST_NAME': forms.TextInput(attrs={'class':'form-control'}),
                  'VEHICLE_CATEGORY': forms.TextInput(attrs={'class':'form-control'}),
                  'Employee' : forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  'BAND_LEVEL' : forms.TextInput(attrs={'class':'form-control'}),
                  'BENEFIT_GROUP': forms.TextInput(attrs={'class':'form-control'}),
                  'COST_CENTER': forms.TextInput(attrs={'class':'form-control'}),
                  'GROUP': forms.TextInput(attrs={'class':'form-control'}),
                  'DIVISION': forms.TextInput(attrs={'class':'form-control'}),
                  'DEPARTMENT': forms.TextInput(attrs={'class':'form-control'}),
                  'SECTION': forms.TextInput(attrs={'class':'form-control'}),
                  'IS_ID': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  'IS_LAST_NAME': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  'IS_FIRST_NAME': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  'LOCATION': forms.TextInput(attrs={'class':'form-control'}),
                  'ORIGINAL_OR_DATE' : forms.TextInput(attrs={'class':'form-control', 'hidden':'true'}),
                  'ACQ_DATE': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
                  'ACQ_COST': forms.TextInput(attrs={'class':'form-control'}),
                  'ASSET_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'EQUIPMENT_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'SAP_PR': forms.TextInput(attrs={'class':'form-control'}),
                  'Vehicle_IVN_no': forms.TextInput(attrs={'class':'form-control'}),
                  'Unit_MATDOC': forms.TextInput(attrs={'class':'form-control'}),
                  'dealer': forms.TextInput(attrs={'class':'form-control'}),
                  'dealer_name': forms.TextInput(attrs={'class':'form-control'}),
                  'PO_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'PLATE_NUMBER_RELEASE_DATE': forms.TextInput(attrs={'class':'form-control'}),
                  'Last_Registration_Date': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
                  'Smoke_Emission_Date': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
                  'COC_Date': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
                  'Remarks': forms.Select(attrs={'class':'form-control', 'choices':'remarks'}),
                  'Status': forms.Select(attrs={'class':'form-control', 'choices':'status'}),
                  'leasing_remark' : forms.Select(attrs={'class':'form-control'})
            }     

class Vmaster(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super(Vmaster, self).__init__(*args, **kwargs)
            self.fields['original_OR_date'].required = False
            
      class Meta:
            model = VehicleMasterList
            exclude = ('ENGINE_NO','CHASSIS_NO','MV_FILE_NO','VEHICLE_TYPE','ASSIGNEE_LAST_NAME','ASSIGNEE_FIRST_NAME','VEHICLE_CATEGORY','Employee_Id',
                  'BAND_LEVEL','BENEFIT_GROUP','COST_CENTER','GROUP','DIVISION','DEPARTMENT','SECTION','IS_ID','IS_LAST_NAME','IS_FIRST_NAME','LOCATION',
                  'ACQ_DATE','ACQ_COST','ASSET_NO','EQUIPMENT_NO','PO_NO',
                  )
            fields = [
                  'PLATE_NO','CS_NO','CR_NAME','PLATE_ENDING','REGISTRATION_MONTH','MODEL','BRAND',
                  'VEHICLE_MAKE','ORIGINAL_OR_DATE','ENGINE_NO','CHASSIS_NO','MV_FILE_NO','VEHICLE_TYPE','ASSIGNEE_LAST_NAME','ASSIGNEE_FIRST_NAME','VEHICLE_CATEGORY','Employee_Id',
                  'BAND_LEVEL','BENEFIT_GROUP','COST_CENTER','GROUP','DIVISION','DEPARTMENT','SECTION','IS_ID','IS_LAST_NAME','IS_FIRST_NAME','LOCATION',
                  'ACQ_DATE','ACQ_COST','ASSET_NO','EQUIPMENT_NO','PO_NO','PLATE_NUMBER_RELEASE_DATE'

            ]

            widgets = {

                  'PLATE_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'CS_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'CR_NAME': forms.TextInput(attrs={'class':'form-control'}),
                  'PLATE_ENDING': forms.TextInput(attrs={'class':'form-control'}),
                  'REGISTRATION_MONTH': forms.TextInput(attrs={'class':'form-control'}),
                  'MODEL': forms.TextInput(attrs={'class':'form-control'}),
                  'BRAND': forms.Select(attrs={'class':'form-control','choices':'Vbrand'}),
                  'VEHICLE_MAKE': forms.TextInput(attrs={'class':'form-control'}),
                  'ORIGINAL_OR_DATE' : forms.TextInput(attrs={'class':'form-control', 'hidden':'true'}),
                  'PLATE_NUMBER_RELEASE_DATE': forms.TextInput(attrs={'class':'form-control', 'hidden':'true'})
            }


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

