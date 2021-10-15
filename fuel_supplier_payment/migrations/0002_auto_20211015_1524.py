# Generated by Django 3.2.3 on 2021-10-15 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel_supplier_payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuel_supplier',
            name='status',
            field=models.CharField(blank=True, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalfuel_supplier',
            name='status',
            field=models.CharField(blank=True, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=100, null=True),
        ),
    ]
