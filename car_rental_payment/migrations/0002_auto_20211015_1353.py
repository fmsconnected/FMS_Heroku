# Generated by Django 3.2.3 on 2021-10-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental_payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrental',
            name='status',
            field=models.CharField(blank=True, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalcarrental',
            name='status',
            field=models.CharField(blank=True, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=100, null=True),
        ),
    ]
