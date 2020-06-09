# Generated by Django 2.1.7 on 2020-06-09 13:50

from django.db import migrations, models
import masterlist.models


class Migration(migrations.Migration):

    dependencies = [
        ('masterlist', '0005_auto_20200609_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalvehiclemasterlist',
            name='Activity_Id',
            field=models.CharField(default=masterlist.models.increment_Activity_Id, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclemasterlist',
            name='Activity_Id',
            field=models.CharField(default=masterlist.models.increment_Activity_Id, max_length=100, null=True),
        ),
    ]
