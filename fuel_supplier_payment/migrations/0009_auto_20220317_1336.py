# Generated by Django 3.2.3 on 2022-03-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel_supplier_payment', '0008_auto_20220317_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel_supplier',
            name='SOA_current_amount',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfuel_supplier',
            name='SOA_current_amount',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
    ]
