# Generated by Django 3.2.3 on 2022-03-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel_supplier_payment', '0003_auto_20211015_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuel_supplier',
            name='Cost_Center',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalfuel_supplier',
            name='Cost_Center',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
