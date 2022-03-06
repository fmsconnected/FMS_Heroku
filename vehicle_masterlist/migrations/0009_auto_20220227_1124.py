# Generated by Django 3.2.3 on 2022-02-27 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterlist', '0001_initial'),
        ('vehicle_masterlist', '0008_auto_20220222_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalvehiclemasterlist',
            name='Employee',
            field=models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='masterlist.employeemasterlist'),
        ),
        migrations.AlterField(
            model_name='vehiclemasterlist',
            name='Employee',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='masterlist.employeemasterlist'),
        ),
    ]