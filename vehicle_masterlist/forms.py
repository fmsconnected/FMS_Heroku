from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import (
      VehicleMasterList
      )


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
            self.fields['IS_NAME'].required = False
            # self.fields['IS_FIRST_NAME'].required = False
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
            self.fields['vehicle_status'].required = False
            self.fields['EMAIL'].required = True
            self.fields['smoke'].required = False
            self.fields['confirmation'].required = False

      class Meta:
            model = VehicleMasterList
            fields = [
                  'PLATE_NO','CS_NO','CR_NAME','PLATE_ENDING','REGISTRATION_MONTH','MODEL','BRAND',
                  'VEHICLE_MAKE','ENGINE_NO','CHASSIS_NO','MV_FILE_NO','VEHICLE_TYPE','ASSIGNEE_LAST_NAME','ASSIGNEE_FIRST_NAME','VEHICLE_CATEGORY','Employee',
                  'BAND_LEVEL','BENEFIT_GROUP','COST_CENTER','GROUP','DIVISION','DEPARTMENT','SECTION','IS_ID','IS_NAME','LOCATION','ORIGINAL_OR_DATE',
                  'ACQ_DATE','ACQ_COST','ASSET_NO','EQUIPMENT_NO', 'SAP_PR','Vehicle_IVN_no','Unit_MATDOC','dealer',
                  'dealer_name','PO_NO','PLATE_NUMBER_RELEASE_DATE','Last_Registration_Date','Smoke_Emission_Date', 'COC_Date', 'Remarks', 'Status', 'leasing_remark','vehicle_status','EMAIL',
                  'smoke','confirmation'
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
                  ('Geely','Geely'),
                  ('MG','MG'),
            )

            status = (
                  ('Yes', 'Yes'),
                  ('No', 'No'),
            )
            vstatus = (
                  ('Sold', 'Sold'),
                  ('Transferred', 'Transferred'),
                  ('Active', 'Active'),
            )
            email = (
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
                  'PLATE_NO': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'CS_NO': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'CR_NAME': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'PLATE_ENDING': forms.TextInput(attrs={'class':'form-control sm-4', 'hidden':'true'}),
                  'REGISTRATION_MONTH': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'MODEL': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'BRAND': forms.Select(attrs={'class':'form-control sm-4','choices':'Vbrand'}),
                  'VEHICLE_MAKE': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'ENGINE_NO': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'CHASSIS_NO': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'MV_FILE_NO': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'VEHICLE_TYPE': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'ASSIGNEE_LAST_NAME': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'ASSIGNEE_FIRST_NAME': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'VEHICLE_CATEGORY': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'Employee' : forms.TextInput(attrs={'class':'form-control sm-4','readonly':'true'}),
                  'BAND_LEVEL' : forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'BENEFIT_GROUP': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'COST_CENTER': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'GROUP': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'DIVISION': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'DEPARTMENT': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'SECTION': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'IS_ID': forms.TextInput(attrs={'class':'form-control sm-4','readonly':'true'}),
                  'IS_NAME': forms.TextInput(attrs={'class':'form-control sm-4','readonly':'true'}),
                  # 'IS_FIRST_NAME': forms.TextInput(attrs={'class':'form-control sm-4','readonly':'true'}),
                  'LOCATION': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'ORIGINAL_OR_DATE' : forms.TextInput(attrs={'class':'form-control sm-4', 'hidden':'true'}),
                  'ACQ_DATE': forms.TextInput(attrs={'class':'form-control sm-4','type':'date'}),
                  'ACQ_COST': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'ASSET_NO': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'EQUIPMENT_NO': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'SAP_PR': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'Vehicle_IVN_no': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'Unit_MATDOC': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'dealer': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'dealer_name': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'PO_NO': forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'PLATE_NUMBER_RELEASE_DATE': forms.TextInput(attrs={'class':'form-control sm-4','type':'date'}),
                  'Last_Registration_Date': forms.TextInput(attrs={'class':'form-control sm-4', 'type':'date'}),
                  'Smoke_Emission_Date': forms.TextInput(attrs={'class':'form-control sm-4', 'type':'date'}),
                  'COC_Date': forms.TextInput(attrs={'class':'form-control sm-4', 'type':'date'}),
                  'Remarks': forms.Select(attrs={'class':'form-control sm-4', 'choices':'remarks'}),
                  'Status': forms.Select(attrs={'class':'form-control sm-4', 'choices':'status'}),
                  'leasing_remark' : forms.TextInput(attrs={'class':'form-control sm-4'}),
                  'vehicle_status':forms.Select(attrs={'class':'form-control sm-4', 'choices':'vstatus'}),
                  'EMAIL': forms.TextInput(attrs={'class':'form-control sm-4','type':'email'}),
                  'smoke':forms.Select(attrs={'class':'form-control sm-4', 'choices':'email'}),
                  'confirmation':forms.Select(attrs={'class':'form-control sm-4', 'choices':'email'}),
            }     

class Vmaster(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super(Vmaster, self).__init__(*args, **kwargs)
            self.fields['original_OR_date'].required = False
            
      class Meta:
            model = VehicleMasterList
            exclude = ('ENGINE_NO','CHASSIS_NO','MV_FILE_NO','VEHICLE_TYPE','ASSIGNEE_LAST_NAME','ASSIGNEE_FIRST_NAME','VEHICLE_CATEGORY','Employee_Id',
                  'BAND_LEVEL','BENEFIT_GROUP','COST_CENTER','GROUP','DIVISION','DEPARTMENT','SECTION','IS_ID','IS_NAME','LOCATION',
                  'ACQ_DATE','ACQ_COST','ASSET_NO','EQUIPMENT_NO','PO_NO',
                  )
            fields = [
                  'PLATE_NO','CS_NO','CR_NAME','PLATE_ENDING','REGISTRATION_MONTH','MODEL','BRAND',
                  'VEHICLE_MAKE','ORIGINAL_OR_DATE','ENGINE_NO','CHASSIS_NO','MV_FILE_NO','VEHICLE_TYPE','ASSIGNEE_LAST_NAME','ASSIGNEE_FIRST_NAME','VEHICLE_CATEGORY','Employee_Id',
                  'BAND_LEVEL','BENEFIT_GROUP','COST_CENTER','GROUP','DIVISION','DEPARTMENT','SECTION','IS_ID','IS_NAME','LOCATION',
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

