# Generated by Django 2.1.7 on 2021-01-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerLog', '0002_cs_log_date_resolved_inital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs_log',
            name='Date_resolved_inital',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
