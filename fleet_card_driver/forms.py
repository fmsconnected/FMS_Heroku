from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import (
    fleet_card_driver

)


class fleetcarddriver_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(fleetcarddriver_form, self).__init__(*args, **kwargs)
        self.fields['STATUS'].required = True
        self.fields['SOA_DATE'].required = False
        self.fields['SOA_NO'].required = False
        self.fields['AMOUNT'].required = False
        self.fields['COST_CENTER'].required = False
        self.fields['DTR_CUTOFF'].required = False
        self.fields['REF_NO'].required = False
        self.fields['REMARKS'].required = False
    class Meta:
        model = fleet_card_driver
        fields = [
            'STATUS',
            'SOA_DATE',
            'SOA_NO',
            'AMOUNT',
            'COST_CENTER',
            'DTR_CUTOFF',
            'REF_NO',
            'REMARKS',
        ]

        status = (
        ('Ongoing','Ongoing'),
        ('Completed','Completed'),
        )

        widgets = {
            'STATUS': forms.Select(attrs={'class': 'form-control', 'choices':'status'}),
            'SOA_DATE': forms.TextInput(attrs={'class': 'form-control', 'type':'date'}),
            'SOA_NO': forms.TextInput(attrs={'class': 'form-control'}),
            'AMOUNT': forms.TextInput(attrs={'class': 'form-control','type':'number'}),
            'COST_CENTER': forms.TextInput(attrs={'class': 'form-control'}),
            'DTR_CUTOFF': forms.TextInput(attrs={'class': 'form-control'}),
            'REF_NO': forms.TextInput(attrs={'class': 'form-control'}),
            'REMARKS': forms.TextInput(attrs={'class': 'form-control'}),
        }


