# Generated by Django 3.2.3 on 2021-09-29 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_report_shell', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shell_report',
            name='Trx_Invoice_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
