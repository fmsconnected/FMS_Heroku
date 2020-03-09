from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import expense_voucher




class voucherform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(voucherform, self).__init__(*args, **kwargs)
        self.fields['new_employee_id'].required = False
        self.fields['new_employee_fname'].required = False
        self.fields['new_employee_lname'].required = False
        self.fields['new_employee_group'].required = False
        self.fields['new_employee_cost'].required = False
        self.fields['employee_fname'].required = False
        self.fields['employee_lname'].required = False
        self.fields['employee_group'].required = False
        self.fields['employee_cost'].required = False
        self.fields['service_amount'].required = False
        self.fields['work_order'].required = False
        self.fields['odometer_start'].required = False
        self.fields['odometer_end'].required = False
        self.fields['v_brand'].required = False
        self.fields['v_make'].required = False
        self.fields['v_fuel_type'].required = False
        self.fields['v_model'].required = False
        self.fields['new_plate_number'].required = False
        self.fields['new_odometer_start'].required = False
        self.fields['new_odometer_end'].required = False
        self.fields['new_v_brand'].required = False
        self.fields['new_v_make'].required = False
        self.fields['new_v_fuel_type'].required = False
        self.fields['new_v_model'].required = False
        self.fields['gt_admin'].required = False
        self.fields['approval_date'].required = False
        self.fields['immediate_supervisor'].required = False
        self.fields['im_approval_date'].required = False
        self.fields['voucher_docs1'].required = False
        self.fields['voucher_docs2'].required = False
        self.fields['voucher_docs3'].required = False
        self.fields['voucher_remarks'].required = False
        self.fields['voucher_forwarded'].required = False
        self.fields['EVO_SLA'].required = False

    class Meta:
        model = expense_voucher
        fields = ['employee_id','employee_fname', 'employee_lname', 'employee_group', 'employee_cost','new_employee_id',
                    'new_employee_fname','new_employee_lname','new_employee_group','new_employee_cost','fleet_area',
                    'received_voucher','trans_type','voucher_no','voucher_amount','voucher_type','fuel_amount','fuel_products',
                    'fuel_liters','service_amount','work_order','plate_number','odometer_start','odometer_end','v_brand',
                    'v_make','v_fuel_type','v_model','new_plate_number','new_odometer_start','new_odometer_end','new_v_brand',
                    'new_v_make','new_v_fuel_type','new_v_model','gt_admin','approval_date','immediate_supervisor','im_approval_date',
                    'voucher_docs1','voucher_docs2','voucher_docs3','voucher_remarks','voucher_forwarded','EVO_SLA']

        fleet_area= (
            ('The Globe Tower','The Globe Tower'),
            ('Visayas-Mindanao','Visayas-Mindanao')
        )
        trans= (
            ('Gas Reimbursements','Gas Reimbursements'),
            ('Car Parts Replacement','Car Parts Replacement'),
            ('GR and CPR','GR and CPR')
        )
        voucher_type= (
            ('Expense Voucher','Expense Voucher'),
            ('Petty Cash Voucher','Petty Cash Voucher'),
            ('EV and PCV','EV and PCV')
        )
        brand= (
            ('BMW','BMW'),
            ('Chevrolet','Chevrolet'),
            ('Chrysler','Chrysler'),
            ('Ford','Ford'),
            ('Honda','Honda'),
            ('Hyundai','Hyundai'),
            ('Isuzu','Isuzu'),
            ('Kia','Kia'),
            ('Masda','Masda'),
            ('Mitsubishi','Mitsubishi'),
            ('Nissan','Nissan'),
            ('Peugeot','Peugeot'),
            ('Subaro','Subaro')
        )
        sup= (
            ('Ser Roy Dela Cruz','Ser Roy Dela Cruz'),
            ('Adolfo Carlos Umali','Adolfo Carlos Umali')
        )
        admin= (
            ('Approved','Approved')
        )

        widgets= {
            
            'employee_id': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            'employee_fname': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            'employee_lname': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            'employee_group': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            'employee_cost': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            'new_employee_id': forms.TextInput(attrs={'class':'form-control'}),
            'new_employee_fname': forms.TextInput(attrs={'class':'form-control'}),
            'new_employee_lname': forms.TextInput(attrs={'class':'form-control'}),
            'new_employee_group': forms.TextInput(attrs={'class':'form-control'}),
            'new_employee_cost': forms.TextInput(attrs={'class':'form-control'}),
            'fleet_area': forms.Select(attrs={'class':'form-control','choices':'fleet_area'}),
            'received_voucher': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'trans_type': forms.Select(attrs={'class':'form-control','choices':'trans'}),
            'voucher_no': forms.TextInput(attrs={'class':'form-control'}),
            'voucher_amount': forms.TextInput(attrs={'class':'form-control'}),
            'voucher_type': forms.Select(attrs={'class':'form-control','choices':'voucher_type'}),
            'fuel_amount': forms.TextInput(attrs={'class':'form-control'}),
            'fuel_products': forms.TextInput(attrs={'class':'form-control'}),
            'fuel_liters': forms.TextInput(attrs={'class':'form-control'}),
            'service_amount': forms.TextInput(attrs={'class':'form-control'}),
            'work_order': forms.TextInput(attrs={'class':'form-control'}),
            'plate_number': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            'odometer_start': forms.TextInput(attrs={'class':'form-control'}),
            'odometer_end': forms.TextInput(attrs={'class':'form-control'}),
            'v_brand': forms.Select(attrs={'class':'form-control','choices':'brand','readonly':'true'}),
            'v_make': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            'v_fuel_type': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            'v_model': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
            'new_plate_number': forms.TextInput(attrs={'class':'form-control'}),
            'new_odometer_start': forms.TextInput(attrs={'class':'form-control'}),
            'new_odometer_end': forms.TextInput(attrs={'class':'form-control'}),
            'new_v_brand': forms.Select(attrs={'class':'form-control','choices':'brand'}),
            'new_v_make': forms.TextInput(attrs={'class':'form-control'}),
            'new_v_fuel_type': forms.TextInput(attrs={'class':'form-control'}),
            'new_v_model': forms.TextInput(attrs={'class':'form-control'}),
            'gt_admin': forms.Select(attrs={'class':'form-control','choices':'admin'}),
            'approval_date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'immediate_supervisor': forms.Select(attrs={'class':'form-control','choices':'sup'}),
            'im_approval_date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'voucher_docs1': forms.TextInput(attrs={'class':'form-control'}),
            'voucher_docs2': forms.TextInput(attrs={'class':'form-control'}),
            'voucher_docs3': forms.TextInput(attrs={'class':'form-control'}),
            'voucher_remarks': forms.TextInput(attrs={'class':'form-control'}),
            'voucher_forwarded': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'EVO_SLA': forms.TextInput(attrs={'class':'form-control','value':'3','hidden':'true'})

        }