# Generated by Django 2.1.7 on 2020-11-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_auditentry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditentry',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
