from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import (
    CS_log

)


class CS_form(forms.ModelForm):
    #   def __init__(self, *args, **kwargs):
    # super(CS_form, self).__init__(*args, **kwargs)
    # self.fields['Suffix'].required = False
    # self.fields['Unit'].required = False
    # self.fields['Sub_unit'].required = False

    class Meta:
        model = CS_log
        fields = [
            'Date_received', 'Fleet_member', 'Client_name', 'Email', 'Mobile_no', 'Transaction_type', 'Plate_no', 'Problem'
        ]
        member = (
            ('Shane Santos', 'Shane Santos'),
            ('Francis Dela Cruz', 'Francis Dela Cruz'),
            ('Glaiza Cabillo', 'Glaiza Cabillo'),
            ('Janine Manzo', 'Janine Manzo'),
            ('Jessie Blanquisco', 'Jessie Blanquisco'),
            ('Maribel Evaristo', 'Maribel Evaristo'),
            ('Princess Concepsion', 'Princess Concepsion'),
            ('Stephanie Warde', 'Stephanie Warde'),
            ('Dennis Alonzo', 'Dennis Alonzo'),
        )
        trans_type = (
            ('Accident Report', 'Accident Report'),
            ('Billing', 'Billing'),
            ('Car Rental', 'Car Rental'),
            ('Fleet Card', 'Fleet Card'),
            ('Insurance', 'Insurance'),
            ('Plate Number', 'Plate Number'),
            ('Vehicle Acquisition', 'Vehicle Acquisition'),
            ('Vehicle Disposal', 'Vehicle Disposal'),
            ('Vehicle Leasing', 'Vehicle Leasing'),
            ('Vehicle Registration', 'Vehicle Registration'),
            ('Others', 'Others'),
        )

        widgets = {

            'Date_received': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fleet_member': forms.Select(attrs={'class': 'form-control', 'choices': 'member'}),
            'Client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
            'Mobile_no': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'Transaction_type': forms.Select(attrs={'class': 'form-control', 'choices': 'trans_type'}),
            'Plate_no': forms.TextInput(attrs={'class': 'form-control'}),
            'Problem': forms.TextInput(attrs={'class': 'form-control'})

        }


class CS_formupdate(forms.ModelForm):
    #   def __init__(self, *args, **kwargs):
    # super(CS_form, self).__init__(*args, **kwargs)
    # self.fields['Suffix'].required = False
    # self.fields['Unit'].required = False
    # self.fields['Sub_unit'].required = False

    class Meta:
        model = CS_log
        fields = [
            'Date_received', 'Fleet_member', 'Client_name', 'Email', 'Mobile_no', 'Transaction_type', 'Plate_no', 'Problem', 'Date_resolved', 'Action_taken'
        ]
        member = (
            ('Shane Santos', 'Shane Santos'),
            ('Francis Dela Cruz', 'Francis Dela Cruz'),
            ('Glaiza Cabillo', 'Glaiza Cabillo'),
            ('Janine Manzo', 'Janine Manzo'),
            ('Jessie Blanquisco', 'Jessie Blanquisco'),
            ('Maribel Evaristo', 'Maribel Evaristo'),
            ('Princess Concepsion', 'Princess Concepsion'),
            ('Stephanie Warde', 'Stephanie Warde'),
            ('Dennis Alonzo', 'Dennis Alonzo'),
        )
        trans_type = (
            ('Accident Report', 'Accident Report'),
            ('Billing', 'Billing'),
            ('Car Rental', 'Car Rental'),
            ('Fleet Card', 'Fleet Card'),
            ('Insurance', 'Insurance'),
            ('Plate Number', 'Plate Number'),
            ('Vehicle Acquisition', 'Vehicle Acquisition'),
            ('Vehicle Disposal', 'Vehicle Disposal'),
            ('Vehicle Leasing', 'Vehicle Leasing'),
            ('Vehicle Registration', 'Vehicle Registration'),
            ('Others', 'Others'),
        )

        widgets = {

            'Date_received': forms.TextInput(attrs={'class': 'form-control', 'type': 'date',  'readonly': 'true'}),
            'Fleet_member': forms.Select(attrs={'class': 'form-control', 'readonly': 'true'}),
            'Client_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'readonly': 'true'}),
            'Mobile_no': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'readonly': 'true'}),
            'Transaction_type': forms.Select(attrs={'class': 'form-control', 'readonly': 'true'}),
            'Plate_no': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true'}),
            'Problem': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true'}),
            'Date_resolved': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Action_taken': forms.TextInput(attrs={'class': 'form-control'})


        }
