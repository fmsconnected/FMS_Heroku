# Generated by Django 3.2.3 on 2022-02-27 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_masterlist', '0009_auto_20220227_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalvehiclemasterlist',
            name='Employee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclemasterlist',
            name='Employee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
