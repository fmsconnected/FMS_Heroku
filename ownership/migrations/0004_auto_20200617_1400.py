# Generated by Django 2.1.7 on 2020-06-17 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownership', '0003_historicalbilling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalownership',
            name='Deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalownership',
            name='transfer_fee',
            field=models.CharField(blank=True, choices=[('JXMTSI', 'JXMTSI'), ('Department', 'Department')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='Deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='transfer_fee',
            field=models.CharField(blank=True, choices=[('JXMTSI', 'JXMTSI'), ('Department', 'Department')], max_length=100, null=True),
        ),
    ]