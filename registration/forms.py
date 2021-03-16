from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import (
    Registration,
      )


class Registration_form(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super(Registration_form, self).__init__(*args, **kwargs)
            self.fields['PLATE_NO'].required = False
            self.fields['CS_NO'].required = False
            self.fields['CR_NAME'].required = False
            self.fields['MODEL'].required = False
            self.fields['BRAND'].required = False
            

      class Meta:
            model = Registration
            fields = [
                  'PLATE_NO',
                  'CS_NO',
                  'CR_NAME',
                  'MODEL',
                  'BRAND',
                  'VEHICLE_MAKE',
                  'ENGINE_NO',
                  'CHASSIS_NO',
                  'MV_FILE_NO',
                  'COC',
                  'SMOKE_TPL',
                  'REMARKS_REGISTERED',
                  'DATE_EMAILED',
                  'JUSTIFICATION_REMARKS',
                  'Registration_month',
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
                  'MODEL': forms.TextInput(attrs={'class':'form-control'}),
                  'BRAND': forms.Select(attrs={'class':'form-control','choices':'Vbrand'}),
                  'VEHICLE_MAKE': forms.TextInput(attrs={'class':'form-control'}),
                  'ENGINE_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'CHASSIS_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'MV_FILE_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'COC': forms.TextInput(attrs={'class':'form-control'}),
                  'SMOKE_TPL': forms.TextInput(attrs={'class':'form-control'}),
                  'REMARKS_REGISTERED': forms.TextInput(attrs={'class':'form-control'}),
                  'DATE_EMAILED': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
                  'JUSTIFICATION_REMARKS' : forms.TextInput(attrs={'class':'form-control'}),
                  'Registration_month' : forms.TextInput(attrs={'class':'form-control','hidden':'true'}),
            }     


# class reg_update_Form(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(reg_update_Form, self).__init__(*args, **kwargs)
#         self.fields['Last_Registration_Date'].required = False
#         self.fields['Smoke_Emission_Date'].required = False
#         self.fields['COC_Date'].required = False
#         self.fields['Remarks'].required = True
#     class Meta:
#         model = Registration
#         fields = ['Last_Registration_Date','Smoke_Emission_Date','COC_Date','Remarks', 'Status'
#         ]


#         remarks = (
#             ('Without Last Registration Date','Without Last Registration Date'),
#             ('Without Smoke Emission Date','Without Smoke Emission Date'),
#             ('Without COC Date','Without COC Date'),
#             ('Complete','Complete')
#             )


#         status = (
#             ('Yes', 'Yes'),
#             ('No', 'No'),
#             )

#         widgets= {
#         "Last_Registration_Date": forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
#         "Smoke_Emission_Date": forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
#         "COC_Date": forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
#         "Remarks": forms.Select(attrs={'class':'form-control', 'choices':'remarks'}),
#         "Status" : forms.Select(attrs={'class':'form-control', 'choices':'status'}),
#         }

