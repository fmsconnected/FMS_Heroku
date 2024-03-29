# Generated by Django 3.2.3 on 2021-07-07 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_report', '0002_petron_report_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petron_report',
            name='DiscountAmount',
            field=models.IntegerField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='petron_report',
            name='DiscountPerLitre',
            field=models.IntegerField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='petron_report',
            name='NetAmount',
            field=models.IntegerField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='petron_report',
            name='ProductAmount',
            field=models.IntegerField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='petron_report',
            name='ProductQuantity',
            field=models.IntegerField(blank=True, max_length=254, null=True),
        ),
    ]
