# Generated by Django 2.1.7 on 2020-05-12 01:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import masterlist.models
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('masterlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalLeasing',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Activity_Id', models.CharField(default=masterlist.models.increment_Activity_Id, max_length=100, null=True)),
                ('PLATE_NUMBER', models.CharField(blank=True, max_length=100, null=True)),
                ('CS_NO', models.CharField(blank=True, max_length=100, null=True)),
                ('COMPANY', models.CharField(blank=True, max_length=100, null=True)),
                ('MODEL', models.CharField(blank=True, max_length=100, null=True)),
                ('BRAND', models.CharField(blank=True, choices=[('Honda', 'Honda'), ('Toyota', 'Toyota'), ('Mitsubishi', 'Mitsubishi'), ('Ford', 'Ford'), ('Masda', 'Masda'), ('Isuzu', 'Isuzu'), ('Hyundai', 'Hyundai'), ('Nissan', 'Nissan'), ('SuZuki', 'Suzuki'), ('Chevrolet', 'Chevrolet'), ('Audi', 'Audi'), ('BMW', 'BMW'), ('Bently', 'Bently'), ('Cadillac', 'Cadillac'), ('Chrysler', 'Chrysler'), ('Dodge', 'Dodge'), ('GMC', 'GMC'), ('Genesis', 'Genesis'), ('Jaguar', 'Jaguar'), ('Land Rover', 'Land Rover'), ('Lexus', 'Lexus'), ('Lincoln', 'Lincoln'), ('Lotus', 'Lotus'), ('Maserati', 'Maserati'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Mini', 'Mini'), ('Porsche', 'Porsche'), ('Ram', 'Ram'), ('Rolls-Royce', 'Rolls-Royce'), ('Saab', 'Saab'), ('Scion', 'Scion'), ('Subaru', 'Subaru'), ('Tesla', 'Tesla'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo'), ('Saturn', 'Saturn')], max_length=100, null=True)),
                ('VEHICLE_MAKE', models.CharField(blank=True, max_length=100, null=True)),
                ('VEHICLE_TYPE', models.CharField(blank=True, max_length=100, null=True)),
                ('LAST_NAME_ASSIGNEE', models.CharField(blank=True, max_length=100, null=True)),
                ('FIRST_NAME_ASSIGNEE', models.CharField(blank=True, max_length=100, null=True)),
                ('VEHICLE_CATEGORY', models.CharField(blank=True, max_length=100, null=True)),
                ('COST_CENTER', models.CharField(blank=True, max_length=100, null=True)),
                ('ID_NUMBER', models.CharField(blank=True, max_length=100, null=True)),
                ('BAND', models.CharField(blank=True, max_length=100, null=True)),
                ('GROUP', models.CharField(blank=True, max_length=100, null=True)),
                ('DIVISION', models.CharField(blank=True, max_length=100, null=True)),
                ('DEPARTMENT', models.CharField(blank=True, max_length=100, null=True)),
                ('SECTION', models.CharField(blank=True, max_length=100, null=True)),
                ('IS_EMPLOYEE_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('IS_LASTNAME', models.CharField(blank=True, max_length=100, null=True)),
                ('IS_FIRSTNAME', models.CharField(blank=True, max_length=100, null=True)),
                ('LOCATION', models.CharField(blank=True, max_length=100, null=True)),
                ('AREA', models.CharField(blank=True, max_length=100, null=True)),
                ('ACQUISITION_DATE', models.CharField(blank=True, max_length=100, null=True)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('acquisition_cost', models.CharField(blank=True, max_length=100, null=True)),
                ('months_36', models.CharField(blank=True, max_length=100, null=True)),
                ('amount1', models.CharField(blank=True, max_length=100, null=True)),
                ('date_in_1', models.CharField(blank=True, max_length=100, null=True)),
                ('date_out_1', models.CharField(blank=True, max_length=100, null=True)),
                ('months_24', models.CharField(blank=True, max_length=100, null=True)),
                ('amount_Vat_EX', models.CharField(blank=True, max_length=100, null=True)),
                ('date_in_2', models.CharField(blank=True, max_length=100, null=True)),
                ('date_out_2', models.CharField(blank=True, max_length=100, null=True)),
                ('extension', models.CharField(blank=True, max_length=100, null=True)),
                ('amount2', models.CharField(blank=True, max_length=100, null=True)),
                ('date_in_3', models.CharField(blank=True, max_length=100, null=True)),
                ('date_out_3', models.CharField(blank=True, max_length=100, null=True)),
                ('chasis_no', models.CharField(blank=True, max_length=100, null=True)),
                ('engine_no', models.CharField(blank=True, max_length=100, null=True)),
                ('CONTRACT_NUMBER', models.CharField(blank=True, max_length=20, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical leasing',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AlterField(
            model_name='historicalvehiclemasterlist',
            name='Activity_Id',
            field=models.CharField(default=masterlist.models.increment_Activity_Id, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclemasterlist',
            name='Activity_Id',
            field=models.CharField(default=masterlist.models.increment_Activity_Id, max_length=100, null=True),
        ),
    ]