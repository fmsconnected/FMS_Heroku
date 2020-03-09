from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import vehicle_report


class reportform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(reportform, self).__init__(*args, **kwargs)
        self.fields['v_accident_type'].required = False
        self.fields['support_docs'].required = False
        self.fields['v_model'].required = False
        self.fields['v_make'].required = False
        self.fields['cond_sticker'].required = False
        self.fields['a_employee_fname'].required = False
        self.fields['a_employee_lname'].required = False
        self.fields['a_employee_no'].required = False
        self.fields['a_employee_company'].required = False
        self.fields['a_employee_group'].required = False
        self.fields['a_employee_division'].required = False
        self.fields['a_employee_dept'].required = False
        self.fields['sup_employee_id'].required = False
        self.fields['sup_employee_fname'].required = False
        self.fields['sup_employee_lname'].required = False
        self.fields['inform_assignee'].required = False
        self.fields['date_of_inspection'].required = False
        self.fields['inspection_remarks'].required = False
        self.fields['date_filed_alarm'].required = False
        self.fields['date_cert_received'].required = False
        self.fields['date_forwarded'].required = False
        self.fields['MVAR_SLA'].required = False

    class Meta:
        model = vehicle_report
        # fields = AutoCompleteSelectMultipleField('plate_number', 'v_model','v_make','cond_sticker')
        fields =['received_date','v_accident_type', 'support_docs', 'plate_number', 'v_model','v_make',
        'cond_sticker','a_employee_id','a_employee_fname','a_employee_lname','a_employee_no',
        'a_employee_company','a_employee_group','a_employee_division','a_employee_dept','sup_employee_id','sup_employee_fname','sup_employee_lname',
        'inform_assignee','date_of_inspection','inspection_remarks','date_filed_alarm','date_cert_received','date_forwarded','MVAR_SLA']


        widgets= {
            
            'received_date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'v_accident_type': forms.TextInput(attrs={'class':'form-control'}),
            'support_docs': forms.TextInput(attrs={'class':'form-control'}),
            'plate_number': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
            'v_model': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
            'v_make': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
            'cond_sticker': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
            'a_employee_id': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
            'a_employee_fname': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
            'a_employee_lname': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
            'a_employee_no': forms.TextInput(attrs={'class':'form-control'}),
            'a_employee_company': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
            'a_employee_group': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
            'a_employee_division': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
            'a_employee_dept': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'}),
            'sup_employee_id': forms.TextInput(attrs={'class':'form-control'}),
            'sup_employee_fname': forms.TextInput(attrs={'class':'form-control'}),
            'sup_employee_lname': forms.TextInput(attrs={'class':'form-control'}),
            'inform_assignee': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'date_of_inspection': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'inspection_remarks': forms.TextInput(attrs={'class':'form-control'}),
            'date_filed_alarm': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'date_cert_received': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'date_forwarded': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'MVAR_SLA': forms.TextInput(attrs={'class':'form-control','value':'5','hidden':'true'})

        }