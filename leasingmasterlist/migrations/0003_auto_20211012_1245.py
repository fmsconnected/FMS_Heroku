# Generated by Django 3.2.3 on 2021-10-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasingmasterlist', '0002_auto_20211011_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalleasing',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='leasing',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]