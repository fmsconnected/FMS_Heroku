# Generated by Django 2.1.7 on 2021-04-19 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corrective', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corrective',
            name='VRR_SLA',
        ),
        migrations.RemoveField(
            model_name='historicalcorrective',
            name='VRR_SLA',
        ),
    ]
