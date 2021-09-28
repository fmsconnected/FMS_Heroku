# Generated by Django 3.2.3 on 2021-09-28 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_report_shell', '0002_shell_pivot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shell_pivot',
            old_name='sum_disc_amount',
            new_name='Sum_total_net',
        ),
        migrations.RenameField(
            model_name='shell_pivot',
            old_name='sum_net_amount',
            new_name='sum_delco_gross',
        ),
        migrations.RemoveField(
            model_name='shell_pivot',
            name='sum_product_amount',
        ),
    ]
