# Generated by Django 3.2.3 on 2021-10-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalservice_vehicle',
            name='Status',
            field=models.CharField(blank=True, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='service_vehicle',
            name='Status',
            field=models.CharField(blank=True, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=200, null=True),
        ),
    ]
