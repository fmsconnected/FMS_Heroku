# Generated by Django 3.2.3 on 2021-09-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_auto_20210928_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='fata_monitoring',
            name='Remarks',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalfata_monitoring',
            name='Remarks',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
