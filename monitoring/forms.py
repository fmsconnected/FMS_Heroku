from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Fata_monitoring
from vehicle_masterlist.models import VehicleMasterList




class FATAmonitoringForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FATAmonitoringForm, self).__init__(*args, **kwargs)
        self.fields['Certificate_of_Reg'].required = False
        self.fields['Vehicle_brand'].required = False
        self.fields['Vehicle_model'].required = False
        self.fields['Globe_fixed_asset'].required = False
        self.fields['Innove_fixed_asset'].required = False
        self.fields['Date_endorsed_Globe'].required = False
        self.fields['Date_endorsed_Innove'].required = False
        self.fields['Clearing_accountability'].required = False
        self.fields['Status'].required = True

    class Meta:
        model = Fata_monitoring
        fields = ['Fata_no','Date_transfer', 'Date_received', 'Plate_no', 'Vehicle_make','Vehicle_brand',
                    'Certificate_of_Reg','Vehicle_model','Transferor_employee','Transferor_Fname','Transferor_Lname',
                    'Recipient_Employee','Recipient_Fname','Recipient_Lname','Date_endorsed_Globe','Date_endorsed_Innove',
                    'Clearing_accountability','Globe_fixed_asset','Innove_fixed_asset','Status']
        status =(
            ("Ongoing","Ongoing"),
            ("Completed","Completed")
        )

        widgets= {
            "Fata_no": forms.TextInput(attrs={'class':'form-control','type':'number'}),
            "Date_transfer": forms.TextInput(attrs={'class':'form-control','type':'date'}),
            "Date_received": forms.TextInput(attrs={'class':'form-control','type':'date'}),
            "Plate_no": forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            "Vehicle_make": forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            "Vehicle_brand": forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            "Certificate_of_Reg": forms.TextInput(attrs={'class':'form-control'}),
            "Vehicle_model": forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            "Transferor_employee": forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            "Transferor_Fname": forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            "Transferor_Lname": forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            "Recipient_Employee": forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            "Recipient_Fname": forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            "Recipient_Lname": forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            "Date_endorsed_Globe": forms.TextInput(attrs={'class':'form-control','type':'date'}),
            "Date_endorsed_Innove": forms.TextInput(attrs={'class':'form-control','type':'date'}),
            "Clearing_accountability": forms.TextInput(attrs={'class':'form-control'}),
            "Globe_fixed_asset": forms.TextInput(attrs={'class':'form-control'}),
            "Innove_fixed_asset": forms.TextInput(attrs={'class':'form-control'}),
            "Status":forms.Select(attrs={'class':'form-control','choices':'status'}),

        }
class reg_updateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(reg_updateForm, self).__init__(*args, **kwargs)
        self.fields['Last_Registration_Date'].required = False
        self.fields['Smoke_Emission_Date'].required = False
        self.fields['COC_Date'].required = False
        self.fields['Remarks'].required = True
    class Meta:
        model = VehicleMasterList
        fields = ['Last_Registration_Date','Smoke_Emission_Date','COC_Date','Remarks', 'Status'
        ]


        remarks = (
            ('Without Last Registration Date','Without Last Registration Date'),
            ('Without Smoke Emission Date','Without Smoke Emission Date'),
            ('Without COC Date','Without COC Date'),
            ('Complete','Complete')
            )


        status = (
            ('Yes', 'Yes'),
            ('No', 'No'),
            )

        widgets= {
        "Last_Registration_Date": forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
        "Smoke_Emission_Date": forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
        "COC_Date": forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
        "Remarks": forms.Select(attrs={'class':'form-control', 'choices':'remarks'}),
        "Status" : forms.Select(attrs={'class':'form-control', 'choices':'status'}),
        }



