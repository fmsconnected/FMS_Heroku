# Generated by Django 3.2.3 on 2021-10-20 13:43

from django.db import migrations, models
import request.models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_auto_20210522_2006'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarRentalRequest',
        ),
        migrations.RemoveField(
            model_name='historicalcarrentalrequest',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalservice_vehicle',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='service_vehicle',
        ),
        migrations.AddField(
            model_name='historicalvehicle_repair',
            name='status',
            field=models.CharField(blank=True, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vehicle_repair',
            name='status',
            field=models.CharField(blank=True, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gas_card',
            name='Activity_id',
            field=models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalgas_card',
            name='Activity_id',
            field=models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='HistoricalCarRentalRequest',
        ),
        migrations.DeleteModel(
            name='Historicalservice_vehicle',
        ),
    ]
