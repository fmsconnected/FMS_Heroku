# Generated by Django 2.1.7 on 2021-01-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerLog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cs_log',
            name='Date_resolved_inital',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
