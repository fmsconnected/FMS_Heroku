# Generated by Django 2.1.7 on 2021-01-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerLog', '0009_auto_20210107_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs_log',
            name='Date_resolved_inital',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
