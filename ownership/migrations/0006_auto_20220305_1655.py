# Generated by Django 3.2.3 on 2022-03-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownership', '0005_auto_20220223_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalownership',
            name='date_application',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='date_application',
            field=models.DateField(blank=True, null=True),
        ),
    ]
