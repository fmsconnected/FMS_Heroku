# Generated by Django 3.2.3 on 2022-03-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel_supplier_payment', '0004_auto_20220314_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel_supplier',
            name='SOA_billdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfuel_supplier',
            name='SOA_billdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
