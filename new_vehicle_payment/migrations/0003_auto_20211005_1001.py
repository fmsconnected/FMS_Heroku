# Generated by Django 3.2.3 on 2021-10-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_vehicle_payment', '0002_auto_20211005_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalvehiclepayment',
            name='PO_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalvehiclepayment',
            name='Status',
            field=models.CharField(blank=True, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclepayment',
            name='PO_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclepayment',
            name='Status',
            field=models.CharField(blank=True, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=100, null=True),
        ),
    ]
