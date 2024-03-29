# Generated by Django 3.2.3 on 2021-09-29 06:47

import car_rental_payment.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=car_rental_payment.models.increment_Activity_id, max_length=100, null=True)),
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
                ('I_number', models.CharField(default=car_rental_payment.models.increment_I_number, max_length=100, null=True)),
                ('I_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('R_purpose', models.CharField(blank=True, max_length=100, null=True)),
                ('C_SLA', models.CharField(blank=True, max_length=10, null=True)),
                ('Deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalCarRental',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Activity_id', models.CharField(default=car_rental_payment.models.increment_Activity_id, max_length=100, null=True)),
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
                ('I_number', models.CharField(default=car_rental_payment.models.increment_I_number, max_length=100, null=True)),
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
    ]
