# Generated by Django 3.2.3 on 2021-09-28 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fata_monitoring',
            name='Cr_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalfata_monitoring',
            name='Cr_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
