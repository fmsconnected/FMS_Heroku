# Generated by Django 2.1.7 on 2020-03-31 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import payment.models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarRental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=payment.models.increment_Activity_id, max_length=100, null=True)),
                ('Bill_date', models.CharField(blank=True, max_length=100, null=True)),
                ('Employee_id', models.CharField(blank=True, max_length=100, null=True)),
                ('L_name', models.CharField(blank=True, max_length=100, null=True)),
                ('F_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_company', models.CharField(blank=True, max_length=100, null=True)),
                ('Cost_center', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_initiated', models.DateField(auto_now=True)),
                ('car_provider', models.CharField(blank=True, max_length=100, null=True)),
                ('sqa_number', models.CharField(blank=True, max_length=100, null=True)),
                ('rfp_no2', models.CharField(blank=True, max_length=100, null=True)),
                ('O_Fname', models.CharField(blank=True, max_length=100, null=True)),
                ('O_Lname', models.CharField(blank=True, max_length=100, null=True)),
                ('O_cost_center', models.CharField(blank=True, max_length=100, null=True)),
                ('Plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('V_model', models.CharField(blank=True, max_length=100, null=True)),
                ('V_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('V_make', models.CharField(blank=True, max_length=100, null=True)),
                ('D_vehicle', models.CharField(blank=True, max_length=100, null=True)),
                ('S_rental', models.CharField(blank=True, max_length=100, null=True)),
                ('E_rental', models.CharField(blank=True, max_length=100, null=True)),
                ('R_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('R_Cost', models.CharField(blank=True, max_length=100, null=True)),
                ('G_cost', models.CharField(blank=True, max_length=100, null=True)),
                ('T_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('P_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('Del_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('Dri_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('M_cost', models.CharField(blank=True, max_length=100, null=True)),
                ('O_expenses', models.CharField(blank=True, max_length=100, null=True)),
                ('VAT', models.CharField(blank=True, max_length=100, null=True)),
                ('T_expenses', models.CharField(blank=True, max_length=100, null=True)),
                ('I_number', models.CharField(default=payment.models.increment_I_number, max_length=100, null=True)),
                ('I_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('R_purpose', models.CharField(blank=True, max_length=100, null=True)),
                ('C_SLA', models.CharField(blank=True, max_length=10, null=True)),
                ('Deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Fuel_supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=payment.models.increment_Activity_id, max_length=20, null=True)),
                ('SOA_Date_received', models.CharField(blank=True, max_length=100)),
                ('Fuel_provider', models.CharField(blank=True, max_length=50, null=True)),
                ('SOA_billdate', models.CharField(blank=True, max_length=100)),
                ('SOA_current_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('SOA_outstanding_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('Payee', models.CharField(blank=True, choices=[('Globe', 'Globe'), ('Innove', 'Innove'), ('Byan', 'Bayan')], max_length=10, null=True)),
                ('SOA_attached', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_initiated', models.DateField(auto_now=True)),
                ('Date_forwarded', models.CharField(blank=True, max_length=100)),
                ('F_SLA', models.CharField(blank=True, max_length=10, null=True)),
                ('Deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalCarRental',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Activity_id', models.CharField(default=payment.models.increment_Activity_id, max_length=100, null=True)),
                ('Bill_date', models.CharField(blank=True, max_length=100, null=True)),
                ('Employee_id', models.CharField(blank=True, max_length=100, null=True)),
                ('L_name', models.CharField(blank=True, max_length=100, null=True)),
                ('F_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_company', models.CharField(blank=True, max_length=100, null=True)),
                ('Cost_center', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_initiated', models.DateField(blank=True, editable=False)),
                ('car_provider', models.CharField(blank=True, max_length=100, null=True)),
                ('sqa_number', models.CharField(blank=True, max_length=100, null=True)),
                ('rfp_no2', models.CharField(blank=True, max_length=100, null=True)),
                ('O_Fname', models.CharField(blank=True, max_length=100, null=True)),
                ('O_Lname', models.CharField(blank=True, max_length=100, null=True)),
                ('O_cost_center', models.CharField(blank=True, max_length=100, null=True)),
                ('Plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('V_model', models.CharField(blank=True, max_length=100, null=True)),
                ('V_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('V_make', models.CharField(blank=True, max_length=100, null=True)),
                ('D_vehicle', models.CharField(blank=True, max_length=100, null=True)),
                ('S_rental', models.CharField(blank=True, max_length=100, null=True)),
                ('E_rental', models.CharField(blank=True, max_length=100, null=True)),
                ('R_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('R_Cost', models.CharField(blank=True, max_length=100, null=True)),
                ('G_cost', models.CharField(blank=True, max_length=100, null=True)),
                ('T_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('P_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('Del_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('Dri_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('M_cost', models.CharField(blank=True, max_length=100, null=True)),
                ('O_expenses', models.CharField(blank=True, max_length=100, null=True)),
                ('VAT', models.CharField(blank=True, max_length=100, null=True)),
                ('T_expenses', models.CharField(blank=True, max_length=100, null=True)),
                ('I_number', models.CharField(default=payment.models.increment_I_number, max_length=100, null=True)),
                ('I_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('R_purpose', models.CharField(blank=True, max_length=100, null=True)),
                ('C_SLA', models.CharField(blank=True, max_length=10, null=True)),
                ('Deadline', models.DateTimeField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical car rental',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFuel_supplier',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Activity_id', models.CharField(default=payment.models.increment_Activity_id, max_length=20, null=True)),
                ('SOA_Date_received', models.CharField(blank=True, max_length=100)),
                ('Fuel_provider', models.CharField(blank=True, max_length=50, null=True)),
                ('SOA_billdate', models.CharField(blank=True, max_length=100)),
                ('SOA_current_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('SOA_outstanding_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('Payee', models.CharField(blank=True, choices=[('Globe', 'Globe'), ('Innove', 'Innove'), ('Byan', 'Bayan')], max_length=10, null=True)),
                ('SOA_attached', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_initiated', models.DateField(blank=True, editable=False)),
                ('Date_forwarded', models.CharField(blank=True, max_length=100)),
                ('F_SLA', models.CharField(blank=True, max_length=10, null=True)),
                ('Deadline', models.DateTimeField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical fuel_supplier',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalVehicle_Repair_payment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Activity_id', models.CharField(default=payment.models.increment_Activity_id, max_length=100, null=True)),
                ('request_date', models.DateField(null=True)),
                ('employee', models.CharField(blank=True, max_length=100, null=True)),
                ('cost_center', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('group_section', models.CharField(blank=True, max_length=100, null=True)),
                ('plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('v_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('engine', models.CharField(blank=True, max_length=100, null=True)),
                ('v_make', models.CharField(blank=True, max_length=100, null=True)),
                ('v_model', models.CharField(blank=True, max_length=100, null=True)),
                ('chassis', models.CharField(blank=True, max_length=100, null=True)),
                ('band', models.CharField(blank=True, max_length=100, null=True)),
                ('cond_sticker', models.CharField(blank=True, max_length=100, null=True)),
                ('equipment_no', models.CharField(blank=True, max_length=100, null=True)),
                ('dealership', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.CharField(blank=True, max_length=20, null=True)),
                ('service_type', models.CharField(blank=True, choices=[('Preventive Maintenance', 'Preventive Maintenance'), ('Corective Maitenance', 'Corective Maitenance'), ('Battery', 'Battery'), ('Tire', 'Tire')], max_length=100, null=True)),
                ('date_initiated', models.DateField(blank=True, editable=False)),
                ('rfp_no', models.CharField(blank=True, max_length=100, null=100)),
                ('invoice_number2', models.CharField(blank=True, max_length=100, null=100)),
                ('invoice_date', models.CharField(blank=True, max_length=100, null=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical vehicle_ repair_payment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalVehiclePayment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Activity_id', models.CharField(default=payment.models.increment_Activity_id, max_length=20)),
                ('PO_no', models.CharField(default=payment.models.increment_PO_no, max_length=100)),
                ('A_employee_ID', models.CharField(blank=True, max_length=50, null=True)),
                ('E_First_name', models.CharField(blank=True, max_length=50, null=True)),
                ('E_Last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('V_deliverDate', models.CharField(blank=True, max_length=100, null=True)),
                ('Plate_no', models.CharField(blank=True, max_length=20, null=True)),
                ('V_model', models.CharField(blank=True, max_length=100, null=True)),
                ('V_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('V_make', models.CharField(blank=True, max_length=100, null=True)),
                ('V_dealer', models.CharField(blank=True, max_length=100, null=True)),
                ('LTO_documents', models.CharField(blank=True, max_length=100, null=True)),
                ('Docs_plate_no', models.CharField(blank=True, max_length=50, null=True)),
                ('LTO_stickers', models.CharField(blank=True, max_length=100, null=True)),
                ('Sticker_fields', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_initial', models.CharField(blank=True, max_length=100, null=True)),
                ('First_payment', models.CharField(blank=True, max_length=100, null=True)),
                ('LTO_charges', models.CharField(blank=True, max_length=100, null=True)),
                ('Outstanding_balance', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_final', models.CharField(blank=True, max_length=100, null=True)),
                ('Routing_remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('V_SLA', models.CharField(blank=True, max_length=10, null=True)),
                ('Next_process', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_initiated', models.DateField(blank=True, editable=False)),
                ('rfp_number', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_number', models.CharField(blank=True, max_length=100, null=True)),
                ('equip_no', models.CharField(blank=True, max_length=100, null=True)),
                ('asset_no', models.CharField(blank=True, max_length=100, null=True)),
                ('sap_no', models.CharField(blank=True, max_length=100, null=True)),
                ('mat_no', models.CharField(blank=True, max_length=100, null=True)),
                ('Dealer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Deadline', models.DateTimeField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical vehicle payment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Vehicle_Repair_payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=payment.models.increment_Activity_id, max_length=100, null=True)),
                ('request_date', models.DateField(null=True)),
                ('employee', models.CharField(blank=True, max_length=100, null=True)),
                ('cost_center', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('group_section', models.CharField(blank=True, max_length=100, null=True)),
                ('plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('v_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('engine', models.CharField(blank=True, max_length=100, null=True)),
                ('v_make', models.CharField(blank=True, max_length=100, null=True)),
                ('v_model', models.CharField(blank=True, max_length=100, null=True)),
                ('chassis', models.CharField(blank=True, max_length=100, null=True)),
                ('band', models.CharField(blank=True, max_length=100, null=True)),
                ('cond_sticker', models.CharField(blank=True, max_length=100, null=True)),
                ('equipment_no', models.CharField(blank=True, max_length=100, null=True)),
                ('dealership', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.CharField(blank=True, max_length=20, null=True)),
                ('service_type', models.CharField(blank=True, choices=[('Preventive Maintenance', 'Preventive Maintenance'), ('Corective Maitenance', 'Corective Maitenance'), ('Battery', 'Battery'), ('Tire', 'Tire')], max_length=100, null=True)),
                ('date_initiated', models.DateField(auto_now=True)),
                ('rfp_no', models.CharField(blank=True, max_length=100, null=100)),
                ('invoice_number2', models.CharField(blank=True, max_length=100, null=100)),
                ('invoice_date', models.CharField(blank=True, max_length=100, null=100)),
            ],
        ),
        migrations.CreateModel(
            name='VehiclePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=payment.models.increment_Activity_id, max_length=20)),
                ('PO_no', models.CharField(default=payment.models.increment_PO_no, max_length=100)),
                ('A_employee_ID', models.CharField(blank=True, max_length=50, null=True)),
                ('E_First_name', models.CharField(blank=True, max_length=50, null=True)),
                ('E_Last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('V_deliverDate', models.CharField(blank=True, max_length=100, null=True)),
                ('Plate_no', models.CharField(blank=True, max_length=20, null=True)),
                ('V_model', models.CharField(blank=True, max_length=100, null=True)),
                ('V_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('V_make', models.CharField(blank=True, max_length=100, null=True)),
                ('V_dealer', models.CharField(blank=True, max_length=100, null=True)),
                ('LTO_documents', models.CharField(blank=True, max_length=100, null=True)),
                ('Docs_plate_no', models.CharField(blank=True, max_length=50, null=True)),
                ('LTO_stickers', models.CharField(blank=True, max_length=100, null=True)),
                ('Sticker_fields', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_initial', models.CharField(blank=True, max_length=100, null=True)),
                ('First_payment', models.CharField(blank=True, max_length=100, null=True)),
                ('LTO_charges', models.CharField(blank=True, max_length=100, null=True)),
                ('Outstanding_balance', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_final', models.CharField(blank=True, max_length=100, null=True)),
                ('Routing_remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('V_SLA', models.CharField(blank=True, max_length=10, null=True)),
                ('Next_process', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_initiated', models.DateField(auto_now=True)),
                ('rfp_number', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_number', models.CharField(blank=True, max_length=100, null=True)),
                ('equip_no', models.CharField(blank=True, max_length=100, null=True)),
                ('asset_no', models.CharField(blank=True, max_length=100, null=True)),
                ('sap_no', models.CharField(blank=True, max_length=100, null=True)),
                ('mat_no', models.CharField(blank=True, max_length=100, null=True)),
                ('Dealer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Deadline', models.DateTimeField()),
            ],
        ),
    ]
