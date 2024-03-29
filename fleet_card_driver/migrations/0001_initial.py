# Generated by Django 3.2.3 on 2021-10-06 09:52

from django.db import migrations, models
import fleet_card_driver.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fleet_card_driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=fleet_card_driver.models.increment_Activity_id, max_length=100)),
                ('STATUS', models.CharField(blank=True, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=100, null=True)),
                ('SOA_DATE', models.CharField(blank=True, max_length=100, null=True)),
                ('SOA_NO', models.CharField(blank=True, max_length=100, null=True)),
                ('AMOUNT', models.CharField(blank=True, max_length=100, null=True)),
                ('COST_CENTER', models.CharField(blank=True, max_length=100, null=True)),
                ('DTR_CUTOFF', models.CharField(blank=True, max_length=100, null=True)),
                ('REF_NO', models.CharField(blank=True, max_length=254, null=True)),
                ('REMARKS', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
