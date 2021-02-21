from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import (
    fleet_card

)


class fleet_card_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(fleet_card_form, self).__init__(*args, **kwargs)
        # self.fields['Date_received'].required = True
    # self.fields['Unit'].required = False
    # self.fields['Sub_unit'].required = False

    class Meta:
        model = fleet_card
        fields = [
            'STATUS',
            'RECEIVED_REQUEST',
            'DATE_VERIFIED',
            'DATE_RECEIVED',
            'DATE_ISSUED',
            'WORK_DAYS',
            'CARD_NUMBER', 
            'NAME',
            'COST_CENTER',
            'PLATE_NUMBER',
            'CARD_TYPE',
            'CABONILLA',
            'STATION'
        ]

        station= (
            ('PETRON','PETRON'),
            ('SHELL','SHELL'),
            ('METRO OIL','METRO OIL'),
            ('UNIOIL','UNIOIL'),
            ('PHOENIX','PHOENIX'),
            ('PTT','PTT'),
            ('CLEAN FUEL','CLEAN FUEL'),
            ('CALTEX','CALTEX'),
            ('SEA OIL','SEA OIL'),
        )

        card_type = (
            ('VEHICLE CARD','VEHICLE CARD'),
            ('DUAL CARD','DUAL CARD'),
            ('SINGLE CARD','SINGLE CARD'),
            ('DRIVERS CARD','DRIVERS CARD'),
        )

        widgets = {
            'STATUS': forms.TextInput(attrs={'class': 'form-control'}),
            'RECEIVED_REQUEST':forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'DATE_VERIFIED':forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'DATE_RECEIVED':forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'DATE_ISSUED':forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'WORK_DAYS':forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'CARD_NUMBER': forms.TextInput(attrs={'class': 'form-control'}),
            'NAME':forms.TextInput(attrs={'class': 'form-control'}),
            'COST_CENTER':forms.TextInput(attrs={'class': 'form-control'}),
            'PLATE_NUMBER':forms.TextInput(attrs={'class': 'form-control'}),
            'CARD_TYPE':forms.Select(attrs={'class': 'form-control','choices': 'card_type'}),
            'CABONILLA':forms.TextInput(attrs={'class': 'form-control'}),
            'STATION':forms.Select(attrs={'class': 'form-control','choices': 'station'}),

        }


