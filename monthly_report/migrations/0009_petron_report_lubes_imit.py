# Generated by Django 3.2.3 on 2021-09-29 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_report', '0008_auto_20210929_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='petron_report',
            name='Lubes_imit',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
