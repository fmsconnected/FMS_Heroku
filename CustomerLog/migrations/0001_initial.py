# Generated by Django 2.1.7 on 2020-12-11 11:01

import CustomerLog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CS_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=CustomerLog.models.increment_Activity_id, max_length=100)),
                ('Date_received', CustomerLog.models.MytypeField()),
                ('Fleet_member', models.CharField(blank=True, choices=[('Shane Santos', 'Shane Santos'), ('Francis Dela Cruz', 'Francis Dela Cruz'), ('Glaiza Cabillo', 'Glaiza Cabillo'), ('Janine Manzo', 'Janine Manzo'), ('Jessie Blanquisco', 'Jessie Blanquisco'), ('Maribel Evaristo', 'Maribel Evaristo'), ('Princess Concepsion', 'Princess Concepsion'), ('Stephanie Warde', 'Stephanie Warde'), ('Dennis Alonzo', 'Dennis Alonzo')], max_length=100, null=True)),
                ('Ageing', models.CharField(blank=True, max_length=100)),
                ('Client_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Mobile_no', models.CharField(blank=True, max_length=100, null=True)),
                ('Transaction_type', models.CharField(blank=True, choices=[('Accident Report', 'Accident Report'), ('Billing', 'Billing'), ('Car Rental', 'Car Rental'), ('Fleet Card', 'Fleet Card'), ('Insurance', 'Insurance'), ('Plate Number', 'Plate Number'), ('Vehicle Acquisition', 'Vehicle Acquisition'), ('Vehicle Disposal', 'Vehicle Disposal'), ('Vehicle Leasing', 'Vehicle Leasing'), ('Vehicle Registration', 'Vehicle Registration'), ('Others', 'Others')], max_length=100, null=True)),
                ('Plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('Problem', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_resolved', models.CharField(blank=True, max_length=100)),
                ('Action_taken', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
